import time
from bs4 import BeautifulSoup

hh_filename = "1812111.html"

hh_file = open(hh_filename, 'rb')
cv_file = open("cv_" + hh_filename, 'w', encoding='utf-8')

soup = BeautifulSoup(hh_file, 'html.parser')  # Просим BeautifulSoup "разобрать" полученную
# страничку на элементы, создав объект soup

cvs = soup.find_all(class_="resume-search-item__content-wrapper")
cvids = soup.find_all(class_="bloko-toggle HH-Employer-VacancyResponse-Topic-ExperienceTrigger")

# data-hh-last-experience-id

for line in range(1, len(cvs)):
    cv_file.write("\n\n\n <br>--- CV#:" + str(cvids[line].get('data-hh-last-experience-id')) +
                  " ---<br> \n\n\n")
    cv_file.write(str(cvs[line]))


hh_file.close()
cv_file.close()
