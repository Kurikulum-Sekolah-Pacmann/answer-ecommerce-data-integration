from sqlalchemy import create_engine


def init_engine():
    cred = {
        'host': 'ep-red-bar-a1rghkov-pooler.ap-southeast-1.aws.neon.tech',
        'user': 'neondb_owner',
        'pass': 'HmY1axWMVi8N',
        'db': 'ecommerce_db',
        'port': 5432
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn


def init_dest_engine():
    cred = {
        'host': 'ep-red-bar-a1rghkov-pooler.ap-southeast-1.aws.neon.tech',
        'user': 'neondb_owner',
        'pass': 'HmY1axWMVi8N',
        'db': 'answer_ecommerce_db',
        'port': 5432
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn
