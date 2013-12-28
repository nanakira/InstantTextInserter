# encoding: shift-jis

import copy

import util_win.keygetter as keygetter

import snippet_manager
import snippet_observer
import snippet_loader
import thread_interface

"""
用語定義

短縮形(abbr)        :
定型文(phrase)      :
スニペット(snippet) : 短縮形と定型文の組

"""

class TriggerThread(
    thread_interface.IWatcherThread,
    snippet_observer.IObserver
):
    """
    短縮形の入力を監視する.
    入力されたら対応する定型文を挿入する.

    スニペットデータが更新された時に通知してほしいので,
    Observer を使って実現している.
    """

    # スレッドループの待機時間.
    # キー入力を余すことなく検出するためにも 0.01 くらいは欲しい.
    INTERVAL_SEC = 0.01

    def __init__(self):
        thread_interface.IWatcherThread.__init__(
            self,
            "trigger thread",
            TriggerThread.INTERVAL_SEC
        )

    # implement the thread interface
    # --------------------------------

    def _init(self):
        import os # @note テスト登録用, 用がなければ消す.

        # initialize members
        # --------------------------------

        self._getter = keygetter.KeyGetter()
        self._manager = snippet_manager.SnippetManager()

        # リロードしても良い場合に立つ.
        # リロード後は降ろす.
        self._can_reload = False

        # 通知されたスニペットデータを入れておく領域.
        self._snippet_container = None

        # settings about the snippet loader
        # --------------------------------

        snippet_loader.inst.attach(self)
        snippet_loader.inst.reload()

    def _procedure(self):
        # 通知されていれば再読込する.
        # 毎回条件分岐が走ることになるが性能的には問題無いはず.
        # -> Bool 型の条件分岐は 1000000 回のループで 0.15 秒かかる程度.
        if self._can_reload:
            self._reload()
            self._can_reload = False

        for i in range(keygetter.VK_MAX):
            if self._getter.is_pushed_once(i):
                self._manager.input(i)

    def _term(self):
        pass

    # implement the observer interface
    # --------------------------------

    def notify(self, snippet_container):
        # これだと他の ovserver に通知された snippet_container
        # も変更してしまう(参照渡しなので)恐れがあるため
        # 念のため deepcopy にする.
        # @todo 基底クラス側で上手いこと処理できないかしら?
        #self._snippet_container = snippet_container
        self._snippet_container = copy.deepcopy(snippet_container)
        self._can_reload = True

    # private methos
    # --------------------------------

    def _reload(self):
        """
        スニペットデータを再読込する.
        """
        # 現在登録されてる内容をクリアする.
        # これしないと再読込ではなく append になってしまう.
        self._manager.clear()

        # container からスニペットを一件ずつ取り出して追加.
        # @todo container の型がコードからわかりにくいので何とかしたい.
        for key in self._snippet_container.keys():
            abbr = key
            phrase = self._snippet_container[key]
            self._manager.add(abbr, phrase)

if __name__ == '__main__':
    from time import sleep

    def start(continuesec):
        """
        with文から抜けるために関数にしている.
        関数化すれば return で抜けられる.

        @param continuesec 何秒間動かすか.
        """
        with TriggerThread() as watcher:
            watcher.start()
            sleep(continuesec)
    start(15)

