# extract
from src.integration.extract.erp_legacy import extract_erp
from src.integration.extract.campaign import extract_campaign
from src.integration.extract.product_catalogue import extract_catalogue

# transform
from src.integration.transform.campaign import generate_campaign
from src.integration.transform.campaign_items import generate_campaign_items
from src.integration.transform.category_catalogue import generate_category
from src.integration.transform.product_catalogue import generate_product
from src.integration.transform.tags_catalogue import generate_tags

# load
from src.integration.load.load_data import load_process

if __name__ == "__main__":
    print("===== Start Data Integration =====\n")

    print("===== Start Extract ERP Data =====\n")    
    # extract erp
    df_products = extract_erp(query = "select * from products")
    df_customers = extract_erp(query = "select * from customers")
    df_carts = extract_erp(query = "select * from carts")
    df_carts_items = extract_erp(query = "select * from cartitems")

    print("===== Finished Extract ERP Data =====\n")

    # extract catalogue
    print("===== Start Extract Catalogue JSON Data =====\n")
    df_catalogue_master = extract_catalogue(uri = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/wrangling-bfp-aksel/refs/heads/main/ecommerce_data/Products.json")
    
    print("===== Finished Extract Catalogue JSON Data =====\n")
    
    # extract campaign
    print("===== Start Extract Campaign Data =====\n")
    df_campaign_master = extract_campaign(uri = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/wrangling-bfp-aksel/refs/heads/main/ecommerce_data/Campaigns.xlsx")
    
    print("===== Finished Extract Campaign Data =====\n")
    
    # transform data
    print("===== Start Transform Data =====\n")
    df_categories = generate_category(data = df_catalogue_master)
    df_product_catalogue = generate_product(data = df_catalogue_master, data_categories = df_categories)
    df_tags = generate_tags(data = df_catalogue_master)
    df_campaigns = generate_campaign(data = df_campaign_master)
    df_campaign_items = generate_campaign_items(data = df_campaign_master)
    
    print("===== Finished Transform Data =====\n")
    
    # load data
    print("===== Start Load Data =====\n")
    
    load_process(data = df_products, table_name = "products", schema_name = "dev")
    load_process(data = df_customers, table_name = "customers", schema_name = "dev")
    load_process(data = df_carts, table_name = "carts", schema_name = "dev")
    load_process(data = df_carts_items, table_name = "cart_items", schema_name = "dev")
    load_process(data = df_categories, table_name = "categories", schema_name = "dev")
    load_process(data = df_product_catalogue, table_name = "product_catalogue", schema_name = "dev")
    load_process(data = df_tags, table_name = "tags", schema_name = "dev")
    load_process(data = df_campaigns, table_name = "campaigns", schema_name = "dev")
    load_process(data = df_campaign_items, table_name = "campaign_items", schema_name = "dev")

    print("===== Finished Load Data =====\n")
    
    print("===== Finished Data Integration =====")
