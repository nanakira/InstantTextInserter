# encoding: shift-jis

import os

import util.executer as executer

import commander_interface

import dialog_wrapper
import endhandler
import reloader
import selfinfo

CMD_OPEN_FILE = "open"
CMD_OPEN_DIRECTORY = "dir"
CMD_SHOW_VERSION   = "version"
CMD_QUIT           = "quit"
CMD_RELOAD         = "reload"
CMD_OPEN_SNIPPET_DIRECTORY = "snippet_directory"
CMD_OPEN_HOTKEY_CONFIG = "hotkey_ini"

class StartingPointCommander(commander_interface.ICommander):
    """
    CoR チェインの始点として使うコマンダ.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        return False

    def _interpret(self, command):
        pass

class OpenDirectoryCommander(commander_interface.ICommander):
    """
    インストールフォルダを開く.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_OPEN_DIRECTORY:
            return True
        return False

    def _interpret(self, command=None):
        _executer = executer.Executer()
        _executer.execute([selfinfo.PROGRAM_DIRECTORY])

class OpenFileCommander(commander_interface.ICommander):
    """
    指定ファイルを指定引数で開く.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_OPEN_FILE:
            return True
        return False

    def _interpret(self, command=None):
        """
        command の書式
        (programname),(parameter)
        """
        _executer = executer.Executer()

        _command, _parameter = '', ''
        try:
            _command = command[0]
            _parameter = command[1]
        except IndexError:
            pass

        _executer_arg = [_command]
        if _parameter:
            _executer_arg.append(_parameter)

        if _executer.execute(_executer_arg)==False:
            dialog_wrapper.ok("プログラムの起動に失敗しました\ncmd:%s\nprm:%s" \
                              % (_command, _parameter))

class VersionCommander(commander_interface.ICommander):
    """
    バージョン情報を表示する.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_SHOW_VERSION:
            return True
        return False

    def _interpret(self, command=None):
        dialog_wrapper.ok(selfinfo.PROGRAM_INFO, "バージョン情報")

class ExitCommander(commander_interface.ICommander):
    """
    プログラムを終了する.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_QUIT:
            return True
        return False

    def _interpret(self, command=None):
        endhandler.inst.run()

class ReloadCommander(commander_interface.ICommander):
    """
    設定を再読込する.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_RELOAD:
            return True
        return False

    def _interpret(self, command=None):
        reloader.inst.reload()

class OpenSnippetDirectoryCommander(commander_interface.ICommander):
    """
    スニペットフォルダを開く.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_OPEN_SNIPPET_DIRECTORY:
            return True
        return False

    def _interpret(self, command=None):
        _executer = executer.Executer()
        _executer.execute([selfinfo.SNIPPETFOLDER_FULLPATH])

class OpenHotkeyConfigCommander(commander_interface.ICommander):
    """
    ホットキー設定ファイルを開く.
    """
    def __init__(self, next_commander=None):
        commander_interface.ICommander.__init__(self, next_commander)

    def _can_interpret(self, command):
        if command==CMD_OPEN_HOTKEY_CONFIG:
            return True
        return False

    def _interpret(self, command=None):
        _executer = executer.Executer()
        _executer.execute([selfinfo.HOTKEYCONFIG_FULLPATH])

if __name__ == '__main__':
    pass
