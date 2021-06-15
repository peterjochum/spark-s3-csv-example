

class S3HtmlUploader:
    """
    Creates HTML from a template and uploads it to a S3 bucket
    """

    bucket_name: str

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def upload_number_as_html(self, number):
        file = self.create_html_file(number)
        self.upload(file)

    def create_html_file(self, number):
        """
        Creates the formatted HTML for the sum
        :param number:
        :return: temporary file
        """
        raise NotImplementedError

    def upload(self, file):
        """
        Uploads the file to S3
        :param file: Name of the file
        """
        raise NotImplementedError
