import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexión a la base de datos
db_user = "myuser"
db_password = "mypassword"
db_host = "db"
db_name = "db"

# Crear conexión a la base de datos
connection_str = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
engine = create_engine(connection_str)

# Cargar las tablas en DataFrames
df_venta = pd.read_sql("SELECT * FROM Venta", engine)
df_cliente = pd.read_sql("SELECT * FROM Cliente", engine)

# Verificar las columnas de cada DataFrame
print("Columnas de df_venta:", df_venta.columns)
print("Columnas de df_cliente:", df_cliente.columns)

# Unir las tablas por la columna idcliente
df_merged = df_venta.merge(df_cliente, on="idcliente", how="inner")

# Calcular el valor total por cada venta
df_merged["facTotal"] = df_merged["cantidad"] * df_merged["valorunitario"]

# Agrupar por Nombre de Cliente y sumar las ventas
df_resultado = df_merged.groupby("nombrecliente")["facTotal"].sum().reset_index()

# Seleccionar el cliente con la facturación más alta
cliente_max = df_resultado.nlargest(1, "facTotal")

# Mostrar el resultado
print("El cliente que representó la facturación más alta este año:")
print(cliente_max)
