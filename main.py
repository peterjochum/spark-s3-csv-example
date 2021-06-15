from s3 import S3HtmlUploader
from spark import SparkCsv
import os
import urllib.request

def download_csv(url):
    """
    Downloads CSV to temporary file
    :param url: URL of the CSV
    :return: file location
    """
    #raise NotImplementedError
    csv_local_path = "C:/temp/data.csv"
    if not os.path.exists("C:/temp"):
        os.makedirs("C:/temp")
    urllib.request.urlretrieve(url, csv_local_path)  # Download to disc

def main():
    # Variables
    # TODO: replace with config file
    url = "http://iot.ee.surrey.ac.uk:8080/datasets/traffic/traffic_feb_june/trafficData158324.csv"
    column = "vehicleCount"
    bucket_name = "aws-csv-spark-example"

    # TODO: Download CSV to temporary file
    file = download_csv(url)

    # Create sum
    spark_csv = SparkCsv(file)
    sum = spark_csv.getSum(column)

    # Call S3 component to publish sum
    s3_uploader = S3HtmlUploader(bucket_name)
    s3_uploader.upload_number_as_html(sum)

if __name__ == "__main__":
    main()
