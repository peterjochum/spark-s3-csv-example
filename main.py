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
    print("Reading config from config.yaml")
    cfg = Config()

    print(f"Downloading file from {cfg.url}")
    file = download_csv(cfg.url)

    print(f"Parsing results from {file}")
    spark_csv = SparkCsv(file)
    results = spark_csv.get_sum(cfg.count_column, cfg.timestamp_column)

    print(f"Call S3 component to publish {len(results['day'])} results")
    s3_uploader = S3HtmlUploader(cfg.bucket_name)
    s3_uploader.upload_results_as_html(results)

    print("Finished...")


if __name__ == "__main__":
    main()
