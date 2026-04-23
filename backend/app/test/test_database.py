import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Conexão DIRETA com Supabase realizada com sucesso!")

    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print("PostgreSQL version:", version)

        # Testa se o banco está vazio ou não
        cur.execute("SELECT COUNT(*) FROM pg_tables WHERE schemaname = 'public';")
        tables = cur.fetchone()[0]
        print(f"Número de tabelas no schema public: {tables}")

    conn.close()
    print("Conexão fechada.")

except Exception as e:
    print("❌ Erro na conexão:", e)