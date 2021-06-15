# https://stackoverflow.com/questions/36719039/sum-operation-on-pyspark-dataframe-giving-typeerror-when-type-is-fine
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

# https://stackoverflow.com/questions/34946051/group-spark-dataframe-by-date
# from pyspark.sql.functions import dayofyear

# https://stackoverflow.com/questions/34946051/group-spark-dataframe-by-date
from pyspark.sql import functions as F


class SparkCsv:
    file: str

    def __init__(self, file):
        self.file = file
        self.spark = (
            SparkSession.builder.master("local[1]").appName("foo").getOrCreate()
        )
        self.df = self.spark.read.csv(file, header=True, inferSchema=True)

    def get_sum(self, count_column, timestamp_column) -> dict:
        """
        Calculates the sum of a column
        :param count_column: Name of the column
        :param timestamp_column: Column which contains the timestamp
        :return: Counts of the count column grouped by days
        """
        result = (
            self.df.groupBy(F.date_format(timestamp_column, "yyyy-MM-dd").alias("day"))
            .agg(_sum(count_column).alias("count"))
            .sort("day")
        )
        return result.toPandas().to_dict("list")
