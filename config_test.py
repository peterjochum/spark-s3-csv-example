import unittest

from config import Config


class ConfigTest(unittest.TestCase):
    def test_config_from_file(self):
        config = Config("config-sample.yaml")
        self.assertEqual(config.timestamp_column, "the-timestamp-column")
        self.assertEqual(config.count_column, "the-count-column")
        self.assertEqual(config.url, "http://example.com/your.csv")
        self.assertEqual(config.bucket_name, "your-bucket-name")
