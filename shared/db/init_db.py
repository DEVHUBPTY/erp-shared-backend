import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from dotenv import load_dotenv
from pathlib import Path
from typing import Type
import os
import time

def wait_for_postgres(host, port, user, password, retries=10, delay=3):
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=user,
                password=password,
                host=host,
                port=port
            )
            conn.close()
            print("✅ PostgreSQL está listo para aceptar conexiones.")
            return
        except psycopg2.OperationalError as e:
            print(f"🔄 Esperando PostgreSQL ({attempt+1}/{retries})... Error: {e}")
            time.sleep(delay)
    raise Exception("❌ PostgreSQL no se pudo conectar después de varios intentos.")

def create_db_if_not_exists(env_path: Path = None):
    load_dotenv(dotenv_path=env_path, override=True)

    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.getenv("POSTGRES_PORT")
    DB_NAME = os.getenv("POSTGRES_DB")

    # Esperar que PostgreSQL esté listo
    wait_for_postgres(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f'CREATE DATABASE "{DB_NAME}"')
            print(f"✅ Base de datos '{DB_NAME}' creada correctamente.")
        else:
            print(f"🟢 La base de datos '{DB_NAME}' ya existe.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error al crear/verificar la base de datos:", e)
        raise

def init_async_db(env_path: Path = None):
    create_db_if_not_exists(env_path)

    load_dotenv(dotenv_path=env_path, override=True)

    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.getenv("POSTGRES_PORT")
    DB_NAME = os.getenv("POSTGRES_DB")

    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    engine = create_async_engine(DATABASE_URL, echo=False)
    session_local = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    base: Type[DeclarativeMeta] = declarative_base()

    return engine, session_local, base