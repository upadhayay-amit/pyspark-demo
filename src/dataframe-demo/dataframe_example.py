from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

# Create a dataframe by reading a json file
data_dir = "/Users/amitupadhayay/self-learning/spark/Spark-The-Definitive-Guide/data/flight-data/json/2015-summary.json"

df = spark.read.format("json").load(data_dir)
df.printSchema()
df.select("DEST_COUNTRY_NAME").show(5)


