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

    # Leer la tabla y convertir fecha a datetime directamente
    print("Cargando y procesando datos...")
    df_venta = pd.read_sql("SELECT * FROM Venta", engine)
    df_venta["fecha"] = pd.to_datetime(df_venta["fecha"])

    # Filtrar y calcular el total directamente
    current_year = pd.Timestamp.now().year
    df_venta = df_venta[df_venta["fecha"].dt.year == current_year]
    df_venta["ValorTotal"] = df_venta["cantidad"] * df_venta["valorunitario"]

    # Agrupar por mes y sumar las ventas
    df_resultado = (
        df_venta.groupby(df_venta["fecha"].dt.month)["ValorTotal"]
        .sum()
        .reset_index(name="ValorTotal")
        .rename(columns={"fecha": "Mes"})
    )

    # Mostrar el resultado
    print("Valor total de las ventas mes por mes:")
    print(df_resultado)

except OperationalError as op_err:
    print(f"Error de conexión a la base de datos: {op_err}")
except SQLAlchemyError as db_err:
    print(f"Error relacionado con la base de datos: {db_err}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
finally:
    print("Ejecución del script finalizada.")
