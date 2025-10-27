import unittest
import unittest.mock
from utilitys.short_url_generator import (
    register_url_data, is_unique_url,
    generate_short_url, url_finded)

class TestShortUrlGenerator(unittest.TestCase):

    def setUp(self):
        # Mock database session
        self.db = unittest.mock.MagicMock()

    def test_register_url_data(self):
        original_url = "http://example.com"
        short_url = "abc123"
        result = register_url_data(original_url, short_url, self.db)
        self.assertTrue(result)
        self.db.add.assert_called()
        self.db.commit.assert_called()
        self.db.refresh.assert_called()

    def test_is_unique_url_unique(self):
        self.db.query().filter().first.return_value = None
        result = is_unique_url("unique123", self.db)
        self.assertTrue(result)

    def test_is_unique_url_not_unique(self):
        self.db.query().filter().first.return_value = True
        result = is_unique_url("notunique123", self.db)
        self.assertFalse(result)

    def test_generate_short_url_success(self):
        url_input = unittest.mock.MagicMock()
        url_input.url = "http://example.com"
        self.db.query().filter().first.side_effect = [None]  # Unique on first try
        result = generate_short_url(url_input, self.db)
        self.assertIn("new_url", result)

    def test_url_finded_found(self):
        expected_url = unittest.mock.MagicMock()
        self.db.query().filter().first.return_value = expected_url
        result = url_finded("short123", self.db)
        self.assertEqual(result, expected_url)

    def test_url_finded_not_found(self):
        self.db.query().filter().first.return_value = None
        result = url_finded("short123", self.db)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()