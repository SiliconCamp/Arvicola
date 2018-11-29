import requests
import time
from bs4 import BeautifulSoup

'''
Данный модуль реализует загрузку названий всех компаний, разместивших вакансии на hh.ru по определенному запросу.
Например, все вакансии около определенных станций метро. Или вакансии в той или иной проф.области.

Используемые модули: requests (загрузка веб-страниц), time (контроль затрачиваемого времени и паузы между запросами),  
BeautifulSoup (версия 4, разбор содержимого страниц)

Значения переменных:
hh_url - шаблон поискового GET-запроса, передает параметры и ограничения поиска.
hh_headers - заголовки HTTP-запроса, которые модуль передает серверу hh.ru
hh_curl - поисковый GET-запрос с указанием конкретной страницы поиска для разбора
hh_page - объект, содержащий полученную поисковую страницу
soup - объект BeautifulSoup, содержащий обработанную структуру поисковой страницы
last_page - переменная, которая содержит тэг с номером последней из поисковых страниц по запросу для прохода всех.
hh_filename - имя файла для сохранения результатов
companies_unique - накопительный список уникальных неповторяющихся названий компаний, чтобы исключить повторы.
hh_file - объект для обращения к файлу записи результатов.
page - номер полученной и обрабатываемой поисковой страницы по запросу.
curtime - время начала работы цикла обработки страницы, нужно для вычисления длительности обработки
hh_text - исходный текст поисковой страницы, полученной по запросу. 




'''

hh_url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&items_on_page=100&metro=4.179&" \
         "metro=95.537&metro=97.603&metro=4.172&no_magic=true&order_by=publication_time&page="

hh_headers = {"user-agent": "my-app/0.0.1"}

hh_curl = hh_url + '0'
hh_page = requests.get(hh_curl, headers=hh_headers, timeout=None)
soup = BeautifulSoup(hh_page.text, 'html.parser')
last_page = soup.find_all(class_='bloko-button HH-Pager-Control')
print(last_page[-1].text)

hh_filename = "compparsed.html"
companies_unique = []

hh_file = open(hh_filename, 'a', encoding='utf-8')

for page in range(0, int(last_page[-1].text)):

    curtime = time.time()

    hh_curl = hh_url + str(page)
    print(hh_curl)

    hh_page = requests.get(hh_curl, headers=hh_headers, timeout=None)
    hh_text = hh_page.text
    soup = BeautifulSoup(hh_page.text, 'html.parser')

    line = 0
    companies = soup.find_all(class_='bloko-link bloko-link_secondary')

    while line < len(companies):
        if not str(companies[line].text) in companies_unique:
            hh_file.write(str(companies[line].text) + "<BR>" + "\n")
            companies_unique.append(str(companies[line].text))
        line += 1

    print(time.time() - curtime)
    time.sleep(2)

hh_file.close()


