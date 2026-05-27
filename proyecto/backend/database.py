import psycopg2

def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="StockMind_Final",   
            user="postgres",        
            password="Admin",  
            port="5432"
        )
        return conexion
    except Exception as e:
        print("Error al conectar con la base de datos de Postgres:", e)
        return None