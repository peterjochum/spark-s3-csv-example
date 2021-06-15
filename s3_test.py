import unittest

from s3 import S3HtmlUploader

class S3Test(unittest.TestCase):

    def setUp(self):
        your_test_bucket = "<insert your test bucket>"
        self.s3_upload = S3HtmlUploader(your_test_bucket)

    def test_upload(self):
        result = self.s3_upload.upload("template.html")
        self.assertTrue(result)

    def test_create_html_file(self):
        output_file_name = self.s3_upload.create_html_file(42)
        with open(output_file_name, "r") as file:
            out_str = file.read()
            print(out_str)
            self.assertIn(str(42), out_str)
