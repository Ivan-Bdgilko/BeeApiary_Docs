import unittest
from types import SimpleNamespace

from hooks.homepage_photo import on_page_content, PLACEHOLDER


class HomepagePhotoTests(unittest.TestCase):
    def render(self, html, topic="index.md"):
        return on_page_content(html, SimpleNamespace(file=SimpleNamespace(norm_src_uri=topic)), None, None)

    def test_other_pages_and_images_are_untouched(self):
        html = '<img src="photo.webp">'
        self.assertEqual(self.render(html), html)
        photo = '<img src="beeapiary-system-components.webp" width="1079" height="754">'
        self.assertEqual(self.render(photo, "system/index.md"), photo)

    def test_relative_localized_source_and_alt_survive_with_noscript_fallback(self):
        original = '<img src="../assets/common/system/overview/beeapiary-system-components.webp" alt="A &amp; B" class="doc-photo" width="1079" height="754" loading="lazy" decoding="async">'
        result = self.render(original)
        self.assertIn(PLACEHOLDER, result)
        self.assertIn('data-deferred-src="../assets/common/system/overview/beeapiary-system-components.webp"', result)
        self.assertIn('alt="A &amp; B"', result)
        self.assertIn(original + "</noscript>", result)
        self.assertIn('rootMargin:"300px 0px"', result)

    def test_unexpected_dimensions_or_duplicate_photo_fail(self):
        photo = '<img src="beeapiary-system-components.webp" width="1079" height="754">'
        with self.assertRaises(ValueError):
            self.render(photo + photo)
        with self.assertRaises(ValueError):
            self.render(photo.replace('1079', '1000'))

    def test_original_jpeg_is_supported_for_independent_compression_rollback(self):
        html = '<img src="beeapiary-system-components.jpeg" width="1079" height="754">'
        self.assertIn('data-deferred-src="beeapiary-system-components.jpeg"', self.render(html))
