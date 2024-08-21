import csv
import os
import re
import subprocess
import pandas as pd
import asyncio
from pyppeteer import launch

abs_path = '/home/tim/code/vacancy_pdf'
print(abs_path)

async def html_to_pdf(name, id):
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': 1508, 'height': 2721})
    await page.goto(f'file://{abs_path}/html/{id}/{name}.html')
    await page.pdf({'path': f'./pdf/{id}/{name}.pdf',
                    'printBackground': True,
                    'height': '720mm',
                    'width': '400mm',
                    'margin': {  # Отступы также могут быть заданы здесь
                        'top': '0mm',
                        'bottom': '0mm',
                        'left': '0mm',
                        'right': '0mm'
                }})  # Сохранение в PDF
    await browser.close()



# def convert_html_to_pdf(name, id):
#     subprocess.run([
#         'wkhtmltopdf',
#         '--page-width', '400mm',
#         '--page-height', '720mm',
#         '--margin-top', '0',
#         '--margin-bottom', '0',
#         '--margin-left', '0',
#         '--margin-right', '0',
#         f'./{name}.html',
#         f'./{name}.pdf',
#     ])
    
    



def get_vacancies(category):
    vacancies = []
    with open('./xlsx/1.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row[2].lower(), category.lower())
            if row[2].lower().strip() == category.lower():
                vacancies.append(row)
    sorted_vacancies = sorted(vacancies, key=lambda x: x[4])
    
    return sorted_vacancies

# convert_html_to_pdf('desc', 1)
# get_vacancies(category='Водитель автомобиля')



def sort_vacancies():
    df = pd.read_csv('./xlsx/template.csv')
    df.sort_values(by='category', inplace=True)
    df.to_csv('./xlsx/template.csv', index=False)



def convert_html_to_pdf(name, id):
    asyncio.get_event_loop().run_until_complete(html_to_pdf(name=name, id=id))
    
    
