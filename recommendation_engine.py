import pandas as pd

catalog_items = pd.read_csv('catalog_items.csv')
# purchased_products = pd.read_csv('purchased_producs.csv')
# target_group = pd.read_csv('target_group.csv')
# visited_products = pd.read_csv('visited_products.csv')

print(catalog_items)
# print(purchased_products)
# print(target_group)
# print(visited_products)

num_items = catalog_items['product_id'].nunique()
print(num_items)