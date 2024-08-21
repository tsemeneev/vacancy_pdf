import csv
import datetime
from math import ceil
import os
import shutil
import subprocess

import openpyxl
from PyPDF2 import PdfReader, PdfWriter

from src.create_pdf import convert_html_to_pdf

# from models.sber import get_category




def create_base(id, name):
    with open(f"./html/{id}/{name}.html", "w") as f:
        f.write(
        """
        <html>

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style type="text/css">
    
        body {
            font-family: 'Montserrat';
        }
        table td,
        table th {
            padding: 0;
            max-width: 100%;
            margin: 0px;
            vertical-align: middle;
            align-content: center;
        }


        .pubdate {
            line-height: 1.5;
            text-align: center;
            padding-top: 7pt;
            padding-bottom: 7pt;
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 20px;
            background-color: #0f466b;
            font-size: 23pt;
            font-weight: semibold;
            color: #ffffff;
            vertical-align: middle;
            margin-left: 1000px;
            margin-right: 15px;
            

        }

        .fixed-div {
            position: fixed;
            top: 3350px;    /* Отступ сверху */
            right: 0px;  /* Отступ справа */
            width: 100%; /* Ширина блока */
            height: 50px; /* Высота блока */
            background-color: #fcce38; /* Цвет фона */
            /* Дополнительные стили */
        }

        .fixed-div2 {
            position: sticky;
            top: 305px;    /* Отступ сверху */
            right: 0px;  /* Отступ справа */
            width: 100%; /* Ширина блока */
            height: 4px; /* Высота блока */
            background-color: #fcce38; /* Цвет фона */
            margin-bottom: 20px;
            /* Дополнительные стили */
        }

        .c0 {
            border-right-style: solid;
            padding: 5pt 5pt 5pt 5pt;
            border-bottom-color: #ffffff;
            border-top-width: 1pt;
            border-right-width: 1pt;
            border-left-color: #ffffff;
            vertical-align: middle;
            border-right-color: #ffffff;
            border-left-width: 1pt;
            border-top-style: solid;
            border-left-style: solid;
            border-bottom-width: 1pt;
            width: 179.6pt;
            border-top-color: #ffffff;
            border-bottom-style: solid
        }

        .c9 {
            border-right-style: solid;
            padding: 5pt 5pt 5pt 5pt;
            border-bottom-color: #ffffff;
            border-top-width: 1pt;
            border-right-width: 1pt;
            border-left-color: #ffffff;
            vertical-align: middle;
            border-right-color: #ffffff;
            border-left-width: 1pt;
            border-top-style: solid;
            border-left-style: solid;
            border-bottom-width: 1pt;
            width: 400.7pt;
            border-top-color: #ffffff;
            border-bottom-style: solid
        }

        .c5 {
            color: #4c4b4b;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 26pt;
            font-style: normal
        }

        .c21 {
            color: #4a86e8;
            font-weight: 700;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 22pt;
            font-style: normal
        }

        .c11 {
            padding-top: 0pt;
            padding-bottom: 3pt;
            line-height: 1.1;
            orphans: 2;
            widows: 2;
            text-align: left;
            height: 11pt
        }

        .c2 {
            color: #000000;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 23pt;
            font-style: normal;
            font-weight: 500
        }

        .c22 {
            padding-top: 0pt;
            padding-bottom: 3pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c4 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c12 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            text-align: center;
            height: 11pt
        }

        .c14 {
            text-decoration-skip-ink: none;
            font-size: 12pt;
            -webkit-text-decoration-skip: none;
            color: #364935;
            text-decoration: underline
        }

        .c7 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            text-align: left;
            height: 11pt
        }

        .c16 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            text-align: center;
        }


        .c20 {
            margin-right: 5%;
            margin-left: 5%;
            border-collapse: collapse;
            
        }

        .c8 {
            padding-top: 0pt;
            padding-bottom: 3pt;
            line-height: 1.0;
            text-align: left
        }

        .c17 {
            padding-top: 0pt;
            padding-bottom: 3pt;
            line-height: 1.0;
            text-align: center
        }

        .c6 {
            font-size: 23pt;
            color: #131212;
            font-weight: bold;
        }

        .c24 {
            background-color: #ffffff;
            max-width: 100%;
            padding: 0pt 0pt 0pt 0pt;
            margin: 0pt 0pt 0pt 0pt;
            height: 100%;
            width: 100%;
            height: 430mm;
            width: 320mm;
           

        }

        .c3 {
            color: inherit;
            text-decoration: underline;
            font-size: 23pt;
        }

        .c15 {
            height: 7pt;
            background-color: #f0f0f0;
        }

        .c1 {
            background-color: #ceef9e
        }

        .c19 {
            height: 11pt
        }

        .c18 {
            height: 0pt;
            background-color: #e1e1e1;
            padding: 0px;
            margin: 0px;
        }

        

        p {
            margin: 0;
            color: #000000;
            font-size: 11pt;
        }
        .clickable {
            cursor: pointer;
        }
        .clickable:hover {
            background-color: #f0f0f0
        }
        
    </style>
</head>

<body style="padding: 0%; margin: 0;">
"""
)
        
        
def create_first_head(category, id, name):
    today = datetime.datetime.now().strftime("%d.%m.%Y")
    with open(f'./html/{id}/{name}.html', 'a')as f:
        f.write(
    f"""
       <div style="align-items: left; background-color: #4c4a4a; display: flex; flex-direction: column;">
        <table style="vertical-align: left;">
            <tr>
                <td style="vertical-align: left;">
                    <img src="https://data-parse.ru/logo.jpg"
                        style="width: 350px; height: 350px; border-radius: 200px;
                        margin-bottom: 30px; margin-top: 30px; margin-left: 35px; margin-right: 15px;"
                        alt="">
                
                <td style="vertical-align: middle; padding-left: 35px">
                    <p><span class="montserrat" style="font-size: 46pt; color: #ffffff; 
                        font-weight: bold;"><a href="http://t.me/RabotaVahtoyRU" style="text-decoration: none; color: #ffffff">
                            Актуальные вакансии ведущих компаний России</a></span> </p><br>
                    <p><span class="montserrat" style="font-size: 36pt; color: #ffffff;
                        font-weight: bold;"><a href="http://t.me/RabotaVahtoyRU" style="text-decoration: none; color: #ffffff">
                        Золотодобывающая отрасль</a></span></p>
                    <p><a href="http://t.me/RabotaVahtoyRU" class="montserrat" style="font-size: 36pt; 
                        font-weight: bold; text-decoration: none; color: #ffffff;">
                            Наш канал в Telegram:  @RabotaVahtoyRU</a></p>
                    <p class="montserrat" style="font-size: 20pt;  color: #ffffff; font-style: italic; padding-top: 5px">
                        Нажмите на ссылку чтобы подписаться</p>
                </td>
            </tr>
        </table>
        <p class="fixed-div2"></p>
    </div>
    <div>
        <p class="c11"><span class="c2"></span></p>
        <p class="montserrat" style="background-color: rgba(120, 189, 153, 0.522); padding-left: 5%; padding-top: 10pt; padding-bottom: 10pt;
        font-size: 28pt; font-weight: bold; color: #000000"><span>Категория: {category}</span></p>
        <p class="c11"><span class="c2"></span></p>
        <p class="pubdate">Дата обновления: {today}</p>
        <br>
    </div>
    """
        )

def create_head(name, id):
    with open(f'./html/{id}/{name}.html', 'a') as f:
        f.write(
    f"""
    <div style="align-items: left; background-color: #4c4a4a; display: flex; flex-direction: column;">
        <table style="vertical-align: left;">
            <tr>
                <td style="vertical-align: left;">
                    <img src="https://data-parse.ru/logo.jpg"
                        style="width: 350px; height: 350px; border-radius: 200px;
                        margin-bottom: 30px; margin-top: 30px; margin-left: 35px; margin-right: 15px;"
                        alt="">
                
                <td style="vertical-align: middle; padding-left: 35px">
                    <p><span class="montserrat" style="font-size: 46pt; color: #ffffff; 
                        font-weight: bold;"><a href="http://t.me/RabotaVahtoyRU" style="text-decoration: none; color: #ffffff">
                            Актуальные вакансии ведущих компаний России</a></span> </p><br>
                    <p><span class="montserrat" style="font-size: 36pt; color: #ffffff;
                        font-weight: bold;"><a href="http://t.me/RabotaVahtoyRU" style="text-decoration: none; color: #ffffff">
                        Золотодобывающая отрасль</a></span></p>
                    <p><a href="http://t.me/RabotaVahtoyRU" class="montserrat" style="font-size: 36pt; 
                        font-weight: bold; text-decoration: none; color: #ffffff;">
                            Наш канал в Telegram:  @RabotaVahtoyRU</a></p>
                    <p class="montserrat" style="font-size: 20pt;  color: #ffffff; font-style: italic; padding-top: 5px">
                        Нажмите на ссылку чтобы подписаться</p>
                </td>
            </tr>
        </table>
        <p class="fixed-div2"></p>
    </div>
    
    """
        )
        

def create_page_body(vacancy_data, name, id):
    for vacancy in vacancy_data:
        pubdate = vacancy[0]
        company_name = vacancy[1]
        vacancy_title = vacancy[2]
        salary = vacancy[4]
        manager = vacancy[6]
        if vacancy[7]:
            phones = f"""<span class="c14"><a class="c3" href="https://wa.me/{vacancy[6]}">{vacancy[6]}</a></span>"""
        else:
            phones = 'Можно только отправить резюме. Нажмите ниже "Ссылка на вакансию"'
        
        email = vacancy[9]

        link = vacancy[10]
        
        
        href_link = f'href="{link}"'
        
        with open(f'./html/{id}/{name}.html', 'a') as f:
            f.write(
        f"""
    <p class="c11"><span class="c2"></span></p>
    <table class="c20" style="width: 90%; margin-bottom: 20px; justify-content: center">
        <tr class="c18">
            <td class="c0 c1" colspan="1" rowspan="1">
                <p class="c16"><span class="c5">Вакансия</span></p>
            </td>
            <td class="c0 c1" colspan="1" rowspan="1">
                <p class="c16"><span class="c5">ЗП</span></p>
            </td>
            <td class="c0 c1" colspan="1" rowspan="1">
                <p class="c16"><span class="c5">Компания</span></p>
            </td>
            
        </tr>
        <tr class="c18">
            <td class="c0" colspan="1" rowspan="1">
                <p class="c17"><span
                        class="c2">{vacancy_title}</span></p>
                
            </td>
            <td class="c0" colspan="1" rowspan="1">
                <p class="c16"><span class="c2">{salary}</span></p>
            </td>
            <td class="c0" colspan="1" rowspan="1">
                <p class="c16"><span class="c2">{company_name}</span></p>
            </td>
            </tr>
            <tr class="c15">
                <td class="c9" colspan="1" rowspan="1">
                    <span class="c6">Менеджер: </span><span
                            class="c2">{manager}</span><br>
                    <span class="c6">Почта: </span><span
                    class="c14"><a class="c3" href="mailto:{email}">{email}</a></span><br>
                    <span class="c6">Ссылка на вакансию: </span><span
                            class="c14"><a class="c3" {href_link}>{link}</a></span>
                </td>
                <td class="c9" colspan="3" rowspan="1">
                    <span class="c6">Тел/WA: </span><span
                            class="c2">{phones}</span><br>
                    <span class="c6">Дата публикации: </span>
                            <span class="c2">{pubdate}</span><br>
                 
                    
                </td>
            </tr>
    </table>

        """
            )
            
           
def end(name, id):
    with open(f'./html/{id}/{name}.html', 'a') as file:
        file.write(
    """
        <div class="fixed-div"></div>

        </body>

    </html>
    """
        )
        
        
def xlsx_to_csv(xlsx_file_path, csv_file_path):
    # Открытие .xlsx файла
    workbook = openpyxl.load_workbook(xlsx_file_path)
    
    # Выбор активного листа
    worksheet = workbook.active
    
    # Создание CSV файла и запись данных
    with open(csv_file_path, 'w', newline="", encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        for row in worksheet.iter_rows(values_only=True):
            writer.writerow(row)


def get_vacancies(category):
    vacancies = []
    with open('./xlsx/1.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row[2].lower(), category.lower())
            if row[2].lower().strip() == category.lower():
                vacancies.append(row)
    sorted_vacancies = sorted(vacancies, key=lambda x: x[4].split(' ')[1] if x[4] != '' else '0', reverse=True)
    
    return sorted_vacancies


def create_first_page(category, vacancies, id):
    name = 1
    create_base(id=id, name=name)
    create_first_head(category=category, name=name, id=id)
    create_page_body(vacancy_data=vacancies[0:7], name=name, id=id)
    end(name=name, id=id)
    convert_html_to_pdf(name=name, id=id)


def create_html_file(id, category):
    if not os.path.exists(f'./html/{id}'):
        os.makedirs(f'./html/{id}')
    if not os.path.exists(f'./pdf/{id}'):
        os.makedirs(f'./pdf/{id}')
    vacancies = get_vacancies(category=category)
    if len(vacancies) < 9:
        create_first_page(category, vacancies, id)
        return
    create_first_page(category, vacancies, id)
    create_other_pages(vacancies, id)
    combined_pdf(id)
    return True
    
    
  
def create_other_pages(vacancies, id):
    vacancies_pages = ceil(len(vacancies[7:]) // 8)
    start = 8
    for page in range(2, vacancies_pages + 1):
        create_base(id=id, name=page)
        create_head(name=page, id=id)
        create_page_body(vacancy_data=vacancies[start:start + 8], name=page, id=id)
        end(name=page, id=id)
        start += 8
        convert_html_to_pdf(name=page, id=id)
    


    

# def convert_html_to_pdf(name, id):
#     subprocess.run([
#         'wkhtmltopdf',
#         '--page-width', '400mm',
#         '--page-height', '720mm',
#         '--margin-top', '0',
#         '--margin-bottom', '0',
#         '--margin-left', '0',
#         '--margin-right', '0',
#         f'./html/{id}/{name}.html',
#         f'./pdf/{id}/{name}.pdf',
#     ])


def combined_pdf(id):

    pdf_writer = PdfWriter()

    directory_path = f'./pdf/{id}'

    # Получаем список файлов в указанной директории
    pdf_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    pdf_files.sort()

    # Перебираем список файлов и добавляем каждый из них в итоговый PDF
    for filename in pdf_files:
        print(filename)
        pdf_reader = PdfReader(f'./pdf/{id}/{filename}')
        pdf_writer.add_page(pdf_reader.pages[0])

    # Записываем итоговый PDF в файл
    with open(f'./pdf/{id}/Список вакансий (РаботаВахтой).pdf', 'wb') as out_pdf_file:
        pdf_writer.write(out_pdf_file)
        
        
def del_html_pdf(id):
    shutil.rmtree(f'./html/{id}', ignore_errors=True)
    shutil.rmtree(f'./pdf/{id}', ignore_errors=True)