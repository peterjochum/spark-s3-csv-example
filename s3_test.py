import unittest

import yaml

from s3 import S3HtmlUploader


class S3Test(unittest.TestCase):
    def setUp(self):
        with open("config.yaml") as config_file:
            cfg = yaml.safe_load(config_file)

        your_test_bucket = cfg["bucket_name"]
        self.s3_upload = S3HtmlUploader(your_test_bucket)

    def test_upload(self):
        result = self.s3_upload.upload("test.html")
        self.assertTrue(result)

    def test_format_results(self):
        test_results = {
            "day": ["2020-06-26 13:12:31", "2020-06-29 13:12:31"],
            "count": [31, 36],
        }
        test_results_html = self.s3_upload.format_results(test_results)
        self.assertIn(test_results["day"][0], test_results_html)
        self.assertIn(test_results["day"][1], test_results_html)
        self.assertIn(str(test_results["count"][0]), test_results_html)
        self.assertIn(str(test_results["count"][1]), test_results_html)

    def test_create_html_file(self):
        results = "This should be in the file"
        output_file_name = self.s3_upload.create_html_file(results)
        with open(output_file_name, "r") as file:
            out_str = file.read()
            self.assertIn(results, out_str)
