import pandas as pd

def fill_missing_fisher_products(all_products, fisher_products):
    for i, products_row in all_products.iterrows():
        if pd.isna(products_row['Fisher_product_name']):
            matching_fisher_row = fisher_products[
                fisher_products['Flinn_product_id'] == products_row['Flinn_product_id']]
            if not matching_fisher_row.empty:
                for column in matching_fisher_row.columns:
                    if pd.isna(products_row[column]):
                        all_products.at[i, column] = matching_fisher_row.iloc[0][column]
    return all_products


if __name__ == '__main__':
    all_products = pd.read_csv(r'C:\Users\G6\PycharmProjects\WebScrappingWebPage\Scrapping Scripts\Output\Master_Matched_Products.csv')
    fisher_products = pd.read_csv('Scrapping Scripts\Output\Master_Matched_Fisher_Products.csv')
    updated_products = fill_missing_fisher_products(all_products, fisher_products)
    updated_products.to_csv('Updated_Master_Matched_Products.csv', index=False)
