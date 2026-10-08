"""Regression checks for dates that must not become build dates."""

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("sitemap_hook", Path(__file__).parents[1] / "hooks/sitemap.py")
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class HistoryTests(unittest.TestCase):
    def test_content_reordering_is_significant(self):
        self.assertNotEqual(hook.significant(["First", "Second"]), hook.significant(["Second", "First"]))

    def test_workflow_status_and_whitespace_do_not_advance_date(self):
        history = """__SITEMAP_DATE__2026-10-08T12:00:00+03:00
diff --git a/docs/uk/index.md b/docs/uk/index.md
--- a/docs/uk/index.md
+++ b/docs/uk/index.md
-translation_status: ready
+translation_status: translated
-Text
+Text\x20\x20\x20
__SITEMAP_DATE__2026-10-03T12:00:00+03:00
diff --git a/docs/uk/index.md b/docs/uk/index.md
--- a/docs/uk/index.md
+++ b/docs/uk/index.md
+Text
"""
        self.assertEqual(hook.history_dates(history), {"docs/uk/index.md": "2026-10-03T12:00:00+03:00"})

    def test_pure_rename_follows_original_content_date(self):
        history = """__SITEMAP_DATE__2026-10-08T12:00:00+03:00
diff --git a/docs/uk/old.md b/docs/uk/new.md
similarity index 100%
rename from docs/uk/old.md
rename to docs/uk/new.md
__SITEMAP_DATE__2026-10-03T12:00:00+03:00
diff --git a/docs/uk/old.md b/docs/uk/old.md
+Content
"""
        self.assertEqual(hook.history_dates(history)["docs/uk/new.md"], "2026-10-03T12:00:00+03:00")

    def config(self):
        from types import SimpleNamespace
        return SimpleNamespace(site_url="https://example.com/docs/", plugins={
            "i18n": SimpleNamespace(config=SimpleNamespace(languages=[SimpleNamespace(locale="uk", build=True)]))
        })

    def test_shallow_or_missing_git_omits_dates(self):
        for value in ("true\n", OSError("Git unavailable")):
            with patch.object(hook, "git", side_effect=value if isinstance(value, Exception) else None, return_value=value):
                hook.DATES = {"docs/uk/index.md": "old"}
                hook.on_config(self.config())
                self.assertEqual(hook.DATES, {})

    def test_dirty_source_omits_date(self):
        with patch.object(hook, "git", side_effect=["false\n", "", "docs/uk/index.md\n", ""]), patch.object(
            hook, "history_dates", return_value={"docs/uk/index.md": "2026-10-03", "docs/en/index.md": "2026-10-04"}
        ):
            hook.on_config(self.config())
            self.assertEqual(hook.DATES, {"docs/en/index.md": "2026-10-04"})


if __name__ == "__main__":
    unittest.main()
