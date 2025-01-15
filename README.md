
# Proyecto: Prueba de Ingreso - Soluciones con SQL y PySpark

Este proyecto aborda la optimización y resolución de consultas SQL, así como la implementación de soluciones con Pandas y PySpark para manejar grandes volúmenes de datos en un entorno contenerizado con Docker.

## Descripción

El objetivo principal es analizar, optimizar y resolver problemas de consultas SQL, utilizando Python y tecnologías avanzadas como PySpark para escenarios de Big Data. Además, el proyecto incluye la configuración completa para ejecutar las soluciones en un entorno aislado usando Docker.

## Estructura del Proyecto

```plaintext
Prueba de Ingreso/
├── db/                         # Configuración para la base de datos
├── python/                     # Scripts de Python
│   ├── Dockerfile              # Archivo Dockerfile para contenerización
│   ├── query_1a.py             # Solución del Punto 1(a) en Python
│   ├── query_1b.py             # Solución del Punto 1(b) en Python
│   ├── query_1c.py             # Solución del Punto 1(c) en Python
│   ├── query_solucion_punto2.py# Solución optimizada para el Punto 2 en PySpark
│   ├── requirements.txt        # Dependencias necesarias para Python
├── queries/                    # Consultas SQL originales y optimizadas
│   ├── query_a.sql             # Consulta para el Punto 1(a)
│   ├── query_b.sql             # Consulta para el Punto 1(b)
│   ├── query_c.sql             # Consulta para el Punto 1(c)
│   ├── query_solucion_c.sql    # Consulta optimizada para el Punto 2(c)
├── docker-compose.yml          # Orquestador para servicios Docker
```

## Requisitos del Sistema

- **Docker**: Para ejecutar el proyecto en contenedores.
- **PostgreSQL**: Base de datos para pruebas y ejecución de consultas.
- **Python 3.10+**: Usado para las soluciones con Pandas y PySpark.
- **Java (OpenJDK 11)**: Necesario para ejecutar PySpark.

## Instalación y Ejecución

### Usando Docker

1. **Construir la imagen Docker**:
   Navega al directorio `python` y ejecuta:
   ```bash
   docker build -t prueba_ingreso_python .
   ```

2. **Levantar el entorno completo con `docker-compose`**:
   Desde el directorio principal, ejecuta:
   ```bash
   docker-compose up --build
   ```

3. **Acceder a los contenedores**:
   - Para ejecutar scripts en Python:
     ```bash
     docker exec -it prueba_ingreso_python python query_1a.py
     ```
   - Para ejecutar consultas SQL:
     ```bash
     docker exec -it postgres_db psql -U myuser -d mi_basedatos -f /queries/query_a.sql
     ```

## Funcionalidades

### Soluciones con SQL

- **Query A (`query_a.sql`)**: Calcula el valor total de las ventas por sucursal.
- **Query B (`query_b.sql`)**: Muestra el valor total de las ventas mes por mes.
- **Query C (`query_c.sql`)**: Identifica al cliente con la facturación más alta.
- **Query Solución C (`query_solucion_c.sql`)**: Optimización del Punto 2(c) utilizando CTEs e índices.

### Soluciones en Python

- **`query_1a.py`**: Implementa la solución del Punto 1(a) utilizando Pandas.
- **`query_1b.py`**: Calcula el valor total de ventas por mes usando Pandas.
- **`query_1c.py`**: Identifica al cliente con mayor facturación en Python.
- **`query_solucion_punto2.py`**: Optimización del Punto 2 utilizando PySpark.

## Tecnologías Utilizadas

- **SQL**: Consultas optimizadas para grandes volúmenes de datos.
- **Python**: Implementaciones con Pandas para análisis de datos.
- **PySpark**: Procesamiento distribuido para manejar Big Data.
- **PostgreSQL**: Base de datos relacional.
- **Docker**: Contenerización del entorno.
- **Docker Compose**: Orquestación de múltiples servicios.

## Limitaciones

### Base de Datos para el Punto 2

- Actualmente, no se cuenta con una base de datos con 500 millones de registros para pruebas reales.
- Las soluciones propuestas están diseñadas para escalar eficientemente a datos de gran tamaño utilizando PySpark y optimizaciones en SQL.
- En su lugar, los scripts han sido probados con datasets simulados para validar la lógica y el rendimiento.

## Cómo Personalizar

### Configuración de la Base de Datos

Modifica el archivo `docker-compose.yml`:
```yaml
environment:
   POSTGRES_USER: myuser
   POSTGRES_PASSWORD: mypassword
   POSTGRES_DB: mi_basedatos
```

### Cambiar scripts o consultas

Edita los archivos en las carpetas `python` o `queries`.
