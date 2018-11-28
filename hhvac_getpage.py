import requests
import time
from bs4 import BeautifulSoup

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

for page in range(0, int(last_page[-1].text)):

    curtime = time.time()

    hh_curl = hh_url + str(page)
    print(hh_curl)

    hh_page = requests.get(hh_curl, headers=hh_headers, timeout=None)
    hh_text = hh_page.text
    soup = BeautifulSoup(hh_page.text, 'html.parser')

    hh_file = open(hh_filename, 'a', encoding='utf-8')

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


