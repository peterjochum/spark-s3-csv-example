from config import Config
from s3 import S3HtmlUploader
from spark import SparkCsv
import urllib.request
import tempfile

def download_csv(url):
    """
    Downloads CSV to temporary file
    :param url: URL of the CSV
    :return: file location
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    urllib.request.urlretrieve(url, temp_file.name)
    return temp_file.name


def main():

    cfg = Config()
    # TODO: Download CSV to temporary file
    file = download_csv(cfg.url)

    # Create results
    spark_csv = SparkCsv(file)
    results = spark_csv.get_sum(cfg.count_column, cfg.timestamp_column)
    # TODO: this is an array

    # Call S3 component to publish results
    s3_uploader = S3HtmlUploader(cfg.bucket_name)
    s3_uploader.upload_results_as_html(results)


if __name__ == "__main__":
    main()
