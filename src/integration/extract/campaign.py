import pandas as pd


def extract_campaign(uri: str) -> pd.DataFrame:
    data = pd.read_excel(uri)

    return data
