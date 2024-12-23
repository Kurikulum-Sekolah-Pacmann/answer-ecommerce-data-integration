import pandas as pd


def generate_category(data: pd.DataFrame) -> pd.DataFrame:
    dict_categories = {}

    dict_categories["category_id"] = data['category'].apply(lambda x: x["category_id"]).values.tolist()
    dict_categories["name"] = data['category'].apply(lambda x: x["name"]).values.tolist()

    df_categories = pd.DataFrame(dict_categories)

    df_categories = df_categories.drop_duplicates()

    return df_categories
