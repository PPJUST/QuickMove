# 修复pynput模块中HotKey类的问题，使其能够正确识别小键盘数字

from pynput import keyboard


class HotKeyFix(keyboard.HotKey):
    def __init__(self, keys, on_activate):
        super().__init__(keys, on_activate)

    def press(self, key):
        setattr(key, '_scan', None)
        super().press(key)

    def release(self, key):
        setattr(key, '_scan', None)
        super().release(key)


class GlobalHotKeysFix(keyboard.Listener):
    def __init__(self, hotkeys, *args, **kwargs):
        self._hotkeys = [
            HotKeyFix(HotKeyFix.parse(key), value)
            for key, value in hotkeys.items()]
        super(GlobalHotKeysFix, self).__init__(
            on_press=self._on_press,
            on_release=self._on_release,
            *args,
            **kwargs)

    def _on_press(self, key):
        for hotkey in self._hotkeys:
            hotkey.press(self.canonical(key))

    def _on_release(self, key):
        for hotkey in self._hotkeys:
            hotkey.release(self.canonical(key))
