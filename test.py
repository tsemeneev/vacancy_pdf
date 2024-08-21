import pandas as pd

from src.make_pdf import create_html_file


df = pd.read_excel('./xlsx/1.xlsx')
cats = df['Категория'].unique()
df.to_csv('./xlsx/1.csv', index=False)
for cat in cats:
    if cat == 'nan':
        continue
    create_html_file('11',category=cat)
    break