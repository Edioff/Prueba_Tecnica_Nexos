from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_sub, row_number, lit
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# 1. Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Optimización de Microservicios") \
    .config("spark.sql.shuffle.partitions", 200) \
    .getOrCreate()

try:
    # 2. Configuración de conexión a la base de datos (hipotética)
    # En un entorno con base de datos real, usarías este bloque
    """
    jdbc_url = "jdbc:postgresql://db:5432/db"
    properties = {
        "user": "myuser",
        "password": "mypassword",
        "driver": "org.postgresql.Driver"
    }

    # Cargar datos desde la base de datos
    print("Cargando datos desde la base de datos...")
    df_microservicios = spark.read.jdbc(jdbc_url, "cld_bi_operacion_eng.microservicios_versiones_t", properties=properties)
    df_fecha = spark.read.jdbc(jdbc_url, "cld_bi_operacion_eng.fecha_incio_2_prueba", properties=properties)
    """

    # Generar datos simulados para pruebas
    print("Generando datos simulados...")
    schema_microservicios = StructType([
        StructField("terminal", StringType(), True),
        StructField("codigo_unico", StringType(), True),
        StructField("version_contenedor", StringType(), True),
        StructField("date_monitoring", TimestampType(), True)
    ])

    data_microservicios = [
        ("terminal1", "codigo1", "Android", "2024-12-01 10:00:00"),
        ("terminal2", "codigo2", "iOS", "2024-12-02 15:30:00"),
        ("terminal1", "codigo1", "Android", "2024-12-03 12:45:00"),
        ("terminal3", "codigo3", "Windows", "2024-12-04 08:15:00")
    ]

    df_microservicios = spark.createDataFrame(data_microservicios, schema=schema_microservicios)

    schema_fecha = StructType([
        StructField("fecha_incio", TimestampType(), True)
    ])

    data_fecha = [("2024-12-02 00:00:00",)]
    df_fecha = spark.createDataFrame(data_fecha, schema=schema_fecha)

    # 3. Ajustar la fecha (fecha_incio - 1 día)
    print("Ajustando fechas...")
    fecha_incio = df_fecha.collect()[0]["fecha_incio"]  # Obtener el valor de fecha_incio
    df_microservicios = df_microservicios.withColumn("fecha_ajustada", date_sub(col("date_monitoring"), 1))

    # 4. Filtrar por fecha ajustada
    print("Filtrando datos...")
    df_filtrado = df_microservicios.filter(col("date_monitoring") == fecha_incio)

    # 5. Calcular el ranking
    print("Calculando ranking...")
    window_spec = Window.partitionBy("terminal", "codigo_unico").orderBy(col("date_monitoring").desc())
    df_ranked = df_filtrado.withColumn("rank", row_number().over(window_spec))

    # 6. Seleccionar registros con Rank = 1
    df_final = df_ranked.filter(col("rank") == 1).drop("rank")

    # 7. Agregar columna "serie"
    print("Agregando columna 'serie'...")
    df_final = df_final.withColumn("serie", lit(""))

    # 8. Mostrar el resultado
    print("Resultado final:")
    df_final.show()

    # 9. Guardar en la base de datos (hipotético)
    # Si tuvieras una base de datos, usarías este bloque
    """
    print("Guardando resultados en la base de datos...")
    df_final.write.jdbc(jdbc_url, "cld_bi_operacion_eng.microservicios_gestor_de_terminales", mode="overwrite", properties=properties)
    """

except Exception as e:
    print(f"Error durante la ejecución: {e}")

finally:
    print("Ejecución del script finalizada.")
