import boto3
from boto3.s3.transfer import S3Transfer
from botocore.exceptions import ClientError


template = """
<html>
<head>
    <title>IOT-2021 - Spark - S3</title>
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"
    integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l"
    crossorigin="anonymous">
</head>
<body>
<main role="main">
<h1>Counting results</h1>
<hr>
the_table
</main>
</body>
</html>
"""


class S3HtmlUploader:
    """
    Creates HTML from a template and uploads it to a S3 bucket
    """

    bucket_name: str

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def format_results(self, results) -> str:
        result_str = '<table class="table table-striped">'
        for i in range(len(results["day"])):
            result_str += (
                f"<tr><td>{results['day'][i]}</td><td>{results['count'][i]}</td></tr>"
            )
        result_str += "</table>"
        return result_str

    def upload_results_as_html(self, results):
        """
        Creates a HTML file containing the results
        :param results: Number to render into the file
        :return: True if upload was successful, False otherwise
        """
        results_table = self.format_results(results)
        file = self.create_html_file(results_table)
        return self.upload(file)

    def create_html_file(self, result_str):
        """
        Creates the formatted HTML for the sum
        :param result_str:
        :return: temporary file
        """
        output_file_name = "result_sample.html"
        with open(output_file_name, "w") as file:
            file.write(template.replace("the_table", result_str))
        return output_file_name

    def upload(self, file):
        """
        Uploads the file to S3
        :param file: Name of the file
        """
        # If S3 key was not specified, use file_name
        key = file

        # Upload the file
        s3_client = boto3.client("s3")
        transfer = S3Transfer(s3_client)
        try:
            transfer.upload_file(
                file, self.bucket_name, key, extra_args={"ACL": "public-read"}
            )
            print(f"Uploaded to {s3_client.meta.endpoint_url}/{self.bucket_name}/{key}")
        except ClientError as e:
            print(e)
            return False
        return True
