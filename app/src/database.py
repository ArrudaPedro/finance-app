import psycopg2 as pg
import os
from dotenv import load_dotenv

load_dotenv()

try:
    print("Conectando...")

    connect = pg.connect(
        dbname= os.getenv("DB_NAME"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        host= os.getenv("DB_HOST"),
        port= os.getenv("DB_PORT")
    )

    print("Conectado ao banco de dados!")

    connect.set_client_encoding('utf-8')  # Evita erro de Unicode
    cursor = connect.cursor()

except Exception as e:
    print(f"Error: {e}")
