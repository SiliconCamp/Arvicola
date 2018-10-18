import requests
import time

bash_url = "http://bash.im/random"
bash_headers = {"user-agent": "my-app/0.0.1"}

for generate in range(1, 10):
    bash_filename = str(generate) + "index.html"
    print(bash_filename + ": generating")
    bash_page = requests.get(bash_url, headers=bash_headers, timeout=None)
    bash_text = bash_page.text
    bash_text = bash_text.split("<")

    bash_file = open(bash_filename, 'w', encoding='windows-1251')
    bash_file.write("<")

    for bash_line in bash_text:
        if bash_line.find('class=\"id\"') > 0:
            bash_file.write(bash_line + "</a><")

    bash_file.close()
    time.sleep(10)