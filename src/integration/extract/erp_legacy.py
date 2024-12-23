import pandas as pd
from src.utils.helper import init_engine


def extract_erp(query: str) -> pd.DataFrame:
    try:
        db_engine = init_engine()

        data = pd.read_sql(sql = query,
                           con = db_engine)

        return data

    except Exception as e:
        raise Exception(e)

    finally:
        db_engine.dispose()
