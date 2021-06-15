import logging

import boto3
from botocore.exceptions import ClientError


template = """
<html>
<head>
    <title>IOT-2021 - Spark - S3</title>
</head>
<body>
There are <strong>the_number</strong> vehicles counted in the column <strong>vehicleCount</strong>.
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

    def upload_number_as_html(self, number):
        """
        Creates a HTML file containing the results
        :param number: Number to render into the file
        :return: True if upload was successful, False otherwise
        """
        file = self.create_html_file(number)
        return self.upload(file)

    def create_html_file(self, number):
        """
        Creates the formatted HTML for the sum
        :param number:
        :return: temporary file
        """
        output_file_name = "result.html"
        with open(output_file_name, "w") as file:
            file.write(template.replace("the_number", str(number)))
        return output_file_name

    def upload(self, file):
        """
        Uploads the file to S3
        :param file: Name of the file
        """
        # If S3 object_name was not specified, use file_name
        object_name = file

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file, self.bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
