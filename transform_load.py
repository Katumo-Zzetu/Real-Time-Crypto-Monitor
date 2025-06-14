from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, regexp_replace
from pyspark.sql.types import StructType, StructField, StringType, DecimalType

class CryptoProcessor:
    def __init__(self):
        # PostgreSQL Configuration (Replace placeholders before running)
        self.postgres_url = "jdbc:postgresql://<HOST>:5432/<DATABASE>"
        self.postgres_table = "crypto_prices"
        self.postgres_user = "<USERNAME>"
        self.postgres_password = "<PASSWORD>"

        # Spark Session Initialization
        self.spark = SparkSession.builder \
            .appName("CryptoStreamProcessor") \
            .config("spark.jars", "/path/to/postgresql-driver.jar") \
            .config("spark.driver.extraClassPath", "/path/to/postgresql-driver.jar") \
            .config("spark.executor.extraClassPath", "/path/to/postgresql-driver.jar") \
            .getOrCreate()

    def define_schema(self):
        """ Defines the schema for structured PostgreSQL data """
        return StructType([
            StructField("timestamp", StringType()),
            StructField("symbol", StringType()),
            StructField("price", StringType())
        ])

    def transform_data(self, raw_df):
        """ Transforms raw PostgreSQL data for Grafana visualization """
        return (
            raw_df.select(
                regexp_replace(raw_df.symbol, "-USD", "").alias("symbol"),
                raw_df.price.cast(DecimalType(15, 8)).alias("price"),
                to_timestamp(raw_df.timestamp).alias("timestamp")
            )
        )

    def process_data(self):
        """ Reads PostgreSQL crypto price data for real-time analytics """
        print(f"📥 Reading from PostgreSQL @ {self.postgres_url}\n")

        raw_df = self.spark.read \
            .format("jdbc") \
            .option("url", self.postgres_url) \
            .option("dbtable", self.postgres_table) \
            .option("user", self.postgres_user) \
            .option("password", self.postgres_password) \
            .load()

        clean_df = self.transform_data(raw_df)
        clean_df.show()  # 👈 This will verify that data is loaded properly

if __name__ == "__main__":
    CryptoProcessor().process_data()
