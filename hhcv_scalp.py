import time
from bs4 import BeautifulSoup

hh_filename = "1812111.html"

hh_file = open(hh_filename, 'rb')
cv_file = open("cv_" + hh_filename, 'w', encoding='utf-8')

soup = BeautifulSoup(hh_file, 'html.parser')  # Просим BeautifulSoup "разобрать" полученную
# страничку на элементы, создав объект soup

cvs = soup.find_all(class_="resume-search-item__content-wrapper")

for line in cvs:
    cv_file.write(str(line))
    cv_file.write("\n\n\n <br>------------------------------<br> \n\n\n")

hh_file.close()
cv_file.close()
