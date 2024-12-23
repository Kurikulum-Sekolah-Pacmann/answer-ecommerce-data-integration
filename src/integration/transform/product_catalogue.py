import pandas as pd


def generate_product(data: pd.DataFrame, data_categories: pd.DataFrame) -> pd.DataFrame:
    SELECTED_COLS = ["product_id", "name", "price", "description", "image_url", "category"]

    _df_products = data[SELECTED_COLS].copy()
    
    _df_products["category"] = _df_products["category"].apply(lambda x: x["category_id"])

    df_products = _df_products.rename({"category": "category_id"})

    return df_products
