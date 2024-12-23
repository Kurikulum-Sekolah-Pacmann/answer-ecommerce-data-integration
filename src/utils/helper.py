from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_NAME_ANSWER = os.getenv("DB_NAME_ANSWER")


def init_engine():
    cred = {
        'host': DB_HOST,
        'user': DB_USER,
        'pass': DB_PASS,
        'db': DB_NAME,
        'port': DB_HOST
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn


def init_dest_engine():
    cred = {
        'host': DB_HOST,
        'user': DB_USER,
        'pass': DB_PASS,
        'db': DB_NAME_ANSWER,
        'port': DB_HOST
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn
