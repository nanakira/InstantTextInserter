# encoding: shift-jis

import os
import unittest

import win32con

import util_win.keycode as keycode

import hotkey_loader

class HotkeyEntryTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assertEntry(self, line, exp_name, exp_mod, exp_key):
        hotkey_entry = hotkey_loader.HotkeyEntry(line)
        self.assertEqual(hotkey_entry._name, exp_name)
        self.assertEqual(hotkey_entry._modifier, exp_mod)
        self.assertEqual(hotkey_entry._keycode, exp_key)

    def test_HotkeyEntry(self):
        """
        ����n�͊ȒP�Ƀe�X�g. �]�͂���Ίϓ_��ǉ�����Ƃ���.
        """
        testname = "hoge"

        # �e�C���L�[���������ϊ��ł���
        self.assertEntry(
            testname + "," + "a, k",
            testname, win32con.MOD_ALT, keycode.K
        )
        self.assertEntry(
            testname + "," + "c, insert",
            testname, win32con.MOD_CONTROL, keycode.INSERT
        )
        self.assertEntry(
            testname + "," + "s, enter",
            testname, win32con.MOD_SHIFT, keycode.ENTER
        )
        self.assertEntry(
            testname + "," + "w, esc",
            testname, win32con.MOD_WIN, keycode.ESC
        )

        # �C���L�[�̑g�ݍ��킹���������ϊ��ł���
        # ���ł�, �啶�����������Ȃ����Ƃ�, �󔒗L���Ă��ǂ����Ƃ��m�F.
        self.assertEntry(
            testname + "," + "cs, k", testname,
            win32con.MOD_CONTROL|win32con.MOD_SHIFT,
            keycode.K
        )
        self.assertEntry(
            testname + "," + "   \t cWa   \t , k \t\t  ", testname,
            win32con.MOD_CONTROL|win32con.MOD_WIN|win32con.MOD_ALT,
            keycode.K
        )
        self.assertEntry(
            testname + "," + "aSCw, k", testname,
            win32con.MOD_SHIFT|win32con.MOD_CONTROL| \
            win32con.MOD_WIN|win32con.MOD_ALT,
            keycode.K
        )

        # �ُ�n
        # @todo �ǂ������ꍇ�ɋ����Ȃ�, �Ƃ���̂��l���Ă��� TDD ���悤��.
        # ��)���O����̓_��, modifier�����̓_��, key�����̓_��, etc...

if __name__ == "__main__":
    unittest.main()