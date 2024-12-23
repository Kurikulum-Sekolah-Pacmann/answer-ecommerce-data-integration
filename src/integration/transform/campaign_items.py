import pandas as pd


def generate_campaign_items(data: pd.DataFrame) -> pd.DataFrame:
    _df_campaign_items = data.copy()

    _df_campaign_items["campaign_objects"] = _df_campaign_items["campaign_objects"].str.split(";")
    
    _df_campaign_items = _df_campaign_items.explode(column = "campaign_objects", ignore_index = True)
    
    SELECTED_COLS = ["campaign_id", "campaign_type", "campaign_objects"]

    df_campaign_items = _df_campaign_items[SELECTED_COLS].copy()

    df_campaign_items = df_campaign_items.rename({"campaign_objects": "campaign_item"}, axis = 1)

    return df_campaign_items
