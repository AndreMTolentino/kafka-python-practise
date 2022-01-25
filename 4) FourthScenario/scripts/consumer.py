from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, StructField, IntegerType
from pyspark.sql.functions import explode, split, col, from_json, concat, lit
from pyspark.sql.functions import sum,avg,max,min,mean,count

# Variables
appName = "Python Example - PySpark SellsData"
master = "local[*]"
kafka_topic_name_input = "numtest"
kafka_topic_name_output = "agg"
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
    .option("subscribe", kafka_topic_name_input) \
    .option("startingOffsets", "latest") \
    .load()

# Select only value message
df = df.selectExpr("CAST(value AS STRING)")

# Define Schema
df_schema = StructType([
                StructField("Operation", StringType()),
                StructField("Client", StringType()),
                StructField("Product", StringType()),
                StructField("Quantity", IntegerType())
            ])

# Split json in columns
df_1 = df.withColumn('jsonData', from_json(col('value'), df_schema)).select('jsondata.*')

# Sum quantity of each Product
df_2 = df_1.groupBy("Product").agg(sum("Quantity").alias("Total"))

# Transform columns in a single value
df_3 = df_2.withColumn("value", concat(
    lit('{"Product": '), col("Product"), lit(', {"Total": '), col("Total"), lit('}')))

df_3.printSchema()

df_write_stream = df_3 \
    .selectExpr("CAST(value AS STRING)") \
    .writeStream \
    .format("kafka")  \
    .outputMode("update") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("topic", kafka_topic_name_output) \
    .option('checkpointLocation', 'tmp') \
    .trigger(processingTime='10 seconds') \
    .start()

"""
df_write_stream = df_3.writeStream \
      .outputMode("update") \
      .format("console") \
      .trigger(processingTime='10 seconds') \
      .start()
"""

df_write_stream.awaitTermination()
