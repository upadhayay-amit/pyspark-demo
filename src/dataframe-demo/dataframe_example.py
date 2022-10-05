from pyspark.sql import SparkSession
from pyspark.sql.functions import col,column,expr

spark = SparkSession.builder.appName("test").getOrCreate()

# Create a dataframe by reading a json file
data_dir = "/Users/amitupadhayay/self-learning/spark/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json"

df = spark.read.format("json").load(data_dir)
df.printSchema()
df.select("DEST_COUNTRY_NAME").show(5)

# create a table from dataframe
df.createOrReplaceTempView("dftable")
spark.sql("select count(*) from dftable").show()

df.select(col("DEST_COUNTRY_NAME"),column("DEST_COUNTRY_NAME"),expr("DEST_COUNTRY_NAME")).show(5)
df.select(col("DEST_COUNTRY_NAME"),col("ORIGIN_COUNTRY_NAME")).show(5)
df.select(expr("DEST_COUNTRY_NAME as destination")).show(5)
df.selectExpr("DEST_COUNTRY_NAME as destination").show(2)

df.selectExpr("*", "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as same_country").show(5)
df.selectExpr("*", "count > 10").show(5)






