import requests
import time

bash_url = "http://bash.im/random"
bash_headers = {"user-agent": "my-app/0.0.1"}

for generate in range(1, 3):
    bash_filename = str(generate) + "index.html"
    print(bash_filename + ": generating")
    bash_page = requests.get(bash_url, headers=bash_headers, timeout=None)
    bash_text = bash_page.text
    bash_text = bash_text.split("<")

    bash_file = open(bash_filename, 'w', encoding='windows-1251')

    line = 0
    print("Lines =", len(bash_text))
    while line < len(bash_text):
        if bash_text[line].find("class=\"text\"") > 0:
            bash_file.write("<" + bash_text[line])
        line += 1

    bash_file.close()
    time.sleep(10)