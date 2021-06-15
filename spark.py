

class SparkCsv:
    file: str

    def __init__(self, file, field):
        self.file = file
        # TODO: create dataframe from CSV
        raise NotImplementedError

    def getSum(self, column) -> int:
        """
        Calculates the sum of a column
        :param column: Name of the column
        :return: Sum of all values in the column
        """
        # TODO: build sum from column
        raise NotImplementedError
