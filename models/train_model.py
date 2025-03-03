from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import col

"
# Iniciar Spark
spark = SparkSession.builder.appName('SAS_to_Databricks').getOrCreate()
"
# Cargar dataset
data_path = 'dbfs:/mnt/datasets/dataset.csv'
df = spark.read.csv(data_path, header=True, inferSchema=True)
"
# Preparar los datos
feature_cols = ['edad', 'ingreso']
assembler = VectorAssembler(inputCols=feature_cols, outputCol='features')
df = assembler.transform(df).select(col('features'), col('compra').alias('label'))
"
# Crear y entrenar el modelo
lr = LogisticRegression(featuresCol='features', labelCol='label')
model = lr.fit(df)
"
# Guardar modelo en Databricks
model_path = 'dbfs:/mnt/models/logistic_model'
model.write().overwrite().save(model_path)
print('✅ Modelo entrenado y guardado en:', model_path)
