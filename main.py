import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

url = "https://api.hm.com/search-services/v1/en_us/search/resultpage"
headers = {"User-Agent": "insomnia/9.3.3"}

all_products = []

num_pages = 150

for page in range(1, num_pages + 1):
    querystring = {
        "query": "Clothes",
        "touchPoint": "desktop",
        "page": str(page),
        "pageSize": "36",
        "sort": "RELEVANCE"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    if 'searchHits' in data and 'productList' in data['searchHits']:
        product_list = data['searchHits']['productList']

        for product in product_list:
            all_products.append({
                'id': product.get('id'),
                'productName': product.get('productName'),
                'brandName': product.get('brandName'),
                'url': f"https://www2.hm.com{product.get('url')}",
                'price': product['prices'][0].get('formattedPrice') if 'prices' in product and product['prices'] else None,
                'colorName': product.get('colorName'),
                'productImage': product.get('productImage')
            })

    if not product_list:
        print(f"No more products found on page {page}. Ending scraping.")
        break

df = pd.DataFrame(all_products)

df.to_csv('products.csv', index=False)
df.to_excel('products.xlsx', index=False, engine='openpyxl')

with PdfPages('products.pdf') as pdf:
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.axis('tight')
    ax.axis('off')
    table_data = df.head(30).to_dict('records')
    table = ax.table(cellText=[list(record.values()) for record in table_data],
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(list(range(len(df.columns))))
    pdf.savefig(fig)
    plt.close(fig)

print(f"CSV, Excel, and PDF files created successfully with {len(df)} products.")
