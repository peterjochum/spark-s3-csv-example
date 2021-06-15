import yaml


class Config:
    url: str
    bucket_name: str
    count_column: str
    timestamp_column: str

    def __init__(self, filename="config.yaml"):
        self.init_from_config_file(filename)

    def init_from_config_file(self, filename):
        # Read configuration file
        with open(filename) as config_file:
            cfg = yaml.safe_load(config_file)

        self.url = cfg["url"]
        self.count_column = cfg["count_column"]
        self.timestamp_column = cfg["timestamp_column"]
        self.bucket_name = cfg["bucket_name"]
