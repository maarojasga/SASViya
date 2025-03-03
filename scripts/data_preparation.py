from pyspark.sql import SparkSession

# Iniciar Spark Session
spark = SparkSession.builder.appName("Data Preparation").getOrCreate()

# Cargar datos desde DBFS
data_path = "dbfs:/mnt/datasets/dataset.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Mostrar información del dataset
df.printSchema()
df.show(5)
