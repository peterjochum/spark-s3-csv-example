from s3 import S3HtmlUploader
from spark import SparkCsv


def download_csv(url):
    """
    Downloads CSV to temporary file
    :param url: URL of the CSV
    :return: file location
    """
    raise NotImplementedError

def main():
    # Variables
    # TODO: replace with config file
    url = "http://foo.com/source.csv"
    column = "columnname"
    bucket_name = "my-s3-bucket"

    # TODO: Download CSV to temporary file
    file = download_csv(url)

    # Create sum
    spark_csv = SparkCsv(file)
    sum = spark_csv.getSum(column)

    # Call S3 component to publish sum
    s3_uploader = S3HtmlUploader(bucket_name)
    s3_uploader.upload(sum)

if __name__ == "__main__":
    main()
