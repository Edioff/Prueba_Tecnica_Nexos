import psycopg2
import psycopg2.extras
from faker import Faker
import random
from datetime import datetime, timedelta
from tqdm import tqdm

# Configuración de conexión a PostgreSQL
DB_HOST = "localhost"  # Cambia si es necesario
DB_NAME = "nexos_prueba"  # Asegúrate de usar la BD correcta
DB_USER = "postgres"
DB_PASSWORD = "jond887788"

# Conectar a PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

# Configurar generador de datos aleatorios
faker = Faker()
batch_size = 10000  # Insertar en bloques de 10,000 para mayor eficiencia
total_records = 1000000  # 1 millón de registros

print(f"Iniciando inserción de {total_records} registros...")

# Insertar datos en bloques
for _ in tqdm(range(0, total_records, batch_size)):
    batch_data = [
        (
            f"T{random.randint(1, 1000)}",  # Terminal simulada
            f"C{random.randint(1, 1000000)}",  # Código único
            f"S{random.randint(1, 1000000)}",  # Serial
            random.choice(["TypeA", "TypeB"]),  # Tipo aleatorio
            f"v{random.randint(1, 9)}.{random.randint(0, 9)}",  # Versión contenedor
            f"v{random.randint(1, 9)}.{random.randint(0, 9)}",  # Versión intérprete
            f"v{random.randint(1, 9)}.{random.randint(0, 9)}",  # Versión DLL
            datetime.now() - timedelta(days=random.randint(0, 365))  # Fecha aleatoria en el último año
        )
        for _ in range(batch_size)
    ]

    # Inserción eficiente con execute_values
    insert_query = """
        INSERT INTO cld_bi_operacion_eng.microservicios_versiones_t (
            terminal, codigo_unico, serial, type, version_contenedor,
            version_interprete, version_dll, date_monitoring
        ) VALUES %s;
    """
    psycopg2.extras.execute_values(cursor, insert_query, batch_data)

    conn.commit()

print("✅ Inserción completada con éxito.")

# Cerrar conexión
cursor.close()
conn.close()
