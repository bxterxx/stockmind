import os

import psycopg2

def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", "5432")
        )
        return conexion
    except Exception as e:
        print("Error al conectar con la base de datos de Postgres:", e)
        return None