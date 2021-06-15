import logging

import boto3
from botocore.exceptions import ClientError


template = """
<html>
<head>
    <title>IOT-2021 - Spark - S3</title>
</head>
<body>
<h1>Counting results</h1>
<hr>
the_table

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
        result_str = "<table>"
        for i in range(len(results['day'])):
            result_str += f"<tr><td>{results['day'][i]}</td><td>{results['count'][i]}</td></tr>"
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
        output_file_name = "result.html"
        with open(output_file_name, "w") as file:
            file.write(template.replace("the_table", result_str))
        return output_file_name

    def upload(self, file):
        """
        Uploads the file to S3
        :param file: Name of the file
        """
        # If S3 object_name was not specified, use file_name
        object_name = file

        # Upload the file
        s3_client = boto3.client("s3")
        try:
            response = s3_client.upload_file(file, self.bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
