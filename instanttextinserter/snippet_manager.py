# encoding: shift-jis

import os
from time import sleep

import snippet_paster

class SnippetManager:
    # キーコードに対応する文字をハードコード.
    # 辞書とかだと遅いのでリストで.
    keycode2chara = ['?','?','?','?','?','?','?','?','?','\t','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?',' ','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','0','1','2','3','4','5','6','7','8','9','?','?','?','?','?','?','?','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','?','?','?','?','0','1','2','3','4','5','6','7','8','9','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?',':',';',',','-','.','/','@','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','[','\\',']','^','?','?','?','\\','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?']

    def __init__(self):
        # メンバ変数の初期化
        self.clear()

        self._paster = snippet_paster.SnippetPaster()

    def add(self, abbr, phrase):
        """
        重複内容を渡されても特に検査はしない.
        @todo 重複内容渡された時の挙動の調査, 必要ならガードなり警告出すなり.
        """
        self._abbrlist.append(abbr.upper())
        self._phraselist.append(phrase)
        self._inputlist.append(0)

        self._list_len = len(self._abbrlist)

    def clear(self):
        """
        登録されているスニペット情報をクリアする.
        """
        # i番目に 短縮形i を入れたリスト
        self._abbrlist = []
        # i番目に 短縮形iが何文字目まで入力と一致しているか を入れたリスト
        self._inputlist = []
        # i番目に 定型文i を入れたリスト
        self._phraselist = []
        # リストの長さ.
        # いちいち len で計算すると遅いのでメンバとして保持する.
        # どのリストも同じ長さになるはずなので, 一つだけあればいい.
        self._list_len = 0

    def printlists(self):
        """
        デバッグ用.
        """
        print self._abbrlist
        print self._phraselist
        print self._inputlist

    def input(self, keycode):
        """
        どの短縮形と一致するかを調べ,
        一致したらペースト処理も併せて実行する.
        """
        for i in range(self._list_len):
            abbr_len = len(self._abbrlist[i])

            # IndexErrorを防ぐ
            if self._inputlist[i] == abbr_len:
                self._inputlist[i] = 0
                continue

            # 入力文字が部分一致しているか調べる
            # 一致しなかったら最初からやり直し
            character = SnippetManager.keycode2chara[keycode]
            if self._abbrlist[i][self._inputlist[i]] != character:
                self._inputlist[i] = 0
                continue

            # クエリの最後まで一致していたら完全に一致.
            # 完全一致時の処理を行った後,
            # それまでの部分一致情報を全てクリアする.
            if abbr_len-1 == self._inputlist[i]:
                # デバッグ用
                #print "hit:" + self._abbrlist[i]
                #print "phrase:" + self._phraselist[i]
                self._paster.paste(self._abbrlist[i], self._phraselist[i])
                self._clear_all_input()
                break

            # 比較する場所を一つずらす
            self._inputlist[i] += 1

        # デバッグ用.
        #print self._inputlist

    def _clear_all_input(self):
        for j in range(self._list_len):
            self._inputlist[j] = 0

if __name__ == '__main__':
    pass
