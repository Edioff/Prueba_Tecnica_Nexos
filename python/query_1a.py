import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, SQLAlchemyError

# Configuración de la conexión a la base de datos
db_user = "myuser"
db_password = "mypassword"
db_host = "db"
db_name = "db"

# Crear conexión a la base de datos
connection_str = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

try:
    # Intentar establecer la conexión
    print("Intentando conectar a la base de datos...")
    engine = create_engine(connection_str)
    
    # Probar la conexión con un simple query
    with engine.connect() as connection:
        connection.execute("SELECT 1")
    print("Conexión exitosa.")

    # Cargar las tablas en DataFrames
    print("Cargando datos...")
    df_venta = pd.read_sql("SELECT * FROM Venta", engine)
    df_almacen = pd.read_sql("SELECT * FROM Almacen", engine)

    # Verificar las columnas de cada DataFrame
    print("Columnas de df_venta:", df_venta.columns)
    print("Columnas de df_almacen:", df_almacen.columns)

    # Unir las tablas por la columna idalmacen
    print("Procesando datos...")
    df_merged = df_venta.merge(df_almacen, on="idalmacen", how="inner")

    # Calcular el valor total por cada venta
    df_merged["ValorTotal"] = df_merged["cantidad"] * df_merged["valorunitario"]

    # Agrupar por sucursal y sumar las ventas
    df_resultado = df_merged.groupby("sucursal")["ValorTotal"].sum().reset_index()

    # Mostrar el resultado
    print("Valor total de las ventas en cada sucursal:")
    print(df_resultado)

except OperationalError as op_err:
    print(f"Error de conexión a la base de datos: {op_err}")
except SQLAlchemyError as db_err:
    print(f"Error relacionado con la base de datos: {db_err}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
finally:
    print("Ejecución del script finalizada.")
