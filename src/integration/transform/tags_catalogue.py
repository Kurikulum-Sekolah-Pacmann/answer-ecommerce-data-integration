import pandas as pd


def generate_tags(data: pd.DataFrame) -> pd.DataFrame:
    _df_tags = data.copy()
    
    _df_tags["tags"] = _df_tags["tags"].astype("str")
    
    _df_tags["tags"] = _df_tags["tags"].str.strip('[]').str.split(',').apply(list)
    
    df_tags = _df_tags.explode(column = "tags", ignore_index = True)

    SELECTED_COLS = ["product_id", "tags"]

    df_tags = df_tags[SELECTED_COLS]

    df_tags = df_tags.rename({"tags": "tag"}, axis = 1)
    
    return df_tags
