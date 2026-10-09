"""The Windows cache workaround must leave non-font assets and Linux untouched."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("privacy_compat", Path(__file__).parents[1] / "hooks/privacy_compat.py")
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class PrivacyCompatTests(unittest.TestCase):
    def test_windows_font_css_extension_and_repeated_config(self):
        plugin = SimpleNamespace(_path_to_file=lambda path, config: SimpleNamespace(abs_src_path=path))
        config = SimpleNamespace(plugins={"material/privacy": plugin})
        with patch.object(hook.os, "name", "nt"):
            hook.on_config(config)
            hook.on_config(config)
        self.assertEqual(plugin._path_to_file("fonts.googleapis.com/css.123", config).abs_src_path, "fonts.googleapis.com/css.123.css")
        self.assertEqual(plugin._path_to_file("fonts.gstatic.com/file.woff2", config).abs_src_path, "fonts.gstatic.com/file.woff2")

    def test_linux_does_not_wrap_plugin(self):
        config = SimpleNamespace(plugins={})
        with patch.object(hook.os, "name", "posix"):
            self.assertIs(hook.on_config(config), config)


if __name__ == "__main__":
    unittest.main()
