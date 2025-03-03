from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import col
"
spark = SparkSession.builder.appName('FeatureEngineering').getOrCreate()
df = spark.read.csv('dbfs:/mnt/datasets/dataset.csv', header=True, inferSchema=True)
assembler = VectorAssembler(inputCols=['edad', 'ingreso'], outputCol='features')
df = assembler.transform(df)
df.select('features', col('compra').alias('label')).write.mode('overwrite').parquet('dbfs:/mnt/datasets/processed_data')
print('✅ Feature Engineering completado y guardado en Databricks')
