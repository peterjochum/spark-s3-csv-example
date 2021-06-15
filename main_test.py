import unittest

from main import download_csv

test_csv = (
    "http://iot.ee.surrey.ac.uk:8080/datasets"
    "/traffic/traffic_feb_june/trafficData158324.csv"
)


class MainTestCase(unittest.TestCase):
    def test_download_csv(self):
        file = download_csv(test_csv)
        with open(file) as temp_file:
            downloaded_str = temp_file.read()
            self.assertEqual(len(downloaded_str), 1714582)
