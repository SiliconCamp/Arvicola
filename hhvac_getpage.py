import requests
import time

hh_url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&items_on_page=100&metro=4.179&" \
         "metro=95.537&metro=97.603&metro=4.172&no_magic=true&order_by=publication_time&page="

hh_headers = {"user-agent": "my-app/0.0.1"}

for page in range(0, 12):

    curtime = time.time()

    hh_curl = hh_url + str(page)
    print(hh_curl)

    hh_filename = str(page) + "compparsed.html"

    hh_page = requests.get(hh_curl, headers=hh_headers, timeout=None)
    hh_text = hh_page.text

    hh_file = open(hh_filename, 'w', encoding='utf-8')

    line = 0
    print("Lines =", len(hh_text))
    print(time.time() - curtime)

    hh_file.close()


