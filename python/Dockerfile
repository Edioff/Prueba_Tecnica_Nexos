# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc openjdk-11-jdk-headless curl \
    && rm -rf /var/lib/apt/lists/*

# Configurar Java para Spark
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"

# Copiar requirements.txt e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar PySpark
RUN pip install pyspark

# Copiar el resto del proyecto
COPY . .

# Comando por defecto
CMD ["python", "query_1c.py"]