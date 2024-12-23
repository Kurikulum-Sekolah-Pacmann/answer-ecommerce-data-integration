import pandas as pd


def generate_campaign(data: pd.DataFrame) -> pd.DataFrame:
    SELECTED_COLS = ["campaign_id", "name", "campaign_type", "start_date"]

    df_campaign = data[SELECTED_COLS].copy()
    
    return df_campaign
