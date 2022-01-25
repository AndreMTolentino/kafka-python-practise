from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, StructField
from pyspark.sql.functions import explode, split, col, from_json


# Variables
appName = "Python Example - PySpark SellsData"
master = "local[*]"
kafka_topic_name = "numtest"
kafka_bootstrap_servers = "localhost:9092"


# Create data frame
spark = SparkSession \
    .builder \
    .appName("SellsData") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
    .getOrCreate()


df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "latest") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")

df_schema = StructType([
                StructField("Operation", StringType()),
                StructField("Client", StringType()),
                StructField("Product", StringType()),
                StructField("Quantity", StringType())
            ])

df = df.withColumn('jsonData', from_json(col('value'), df_schema)).select('jsondata.*')

df_write_stream = df \
    .writeStream \
    .format("parquet")  \
    .outputMode("append") \
    .option("path", "outcome") \
    .option('checkpointLocation', 'tmp') \
    .start()


"""
df_write_stream = df.writeStream \
      .outputMode("append") \
      .format("console") \
      .start()
"""

df_write_stream.awaitTermination()
