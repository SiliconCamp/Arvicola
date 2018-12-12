import time
from bs4 import BeautifulSoup

hh_filename = "1812111.html"

hh_file = open("HHSaves\\" + hh_filename, 'rb')


soup = BeautifulSoup(hh_file, 'html.parser')  # Просим BeautifulSoup "разобрать" полученную
# страничку на элементы, создав объект soup

cvs = soup.find_all(class_="resume-search-item__content-wrapper")
cvids = soup.find_all(class_="bloko-toggle HH-Employer-VacancyResponse-Topic-ExperienceTrigger")

# data-hh-last-experience-id

for line in range(0, len(cvs)):
    cv_file = open("CVStore\\cv_" + str(cvids[line].get('data-hh-last-experience-id') + ".html"), 'w', encoding='utf-8')

    cv_file.write("\n\n\n <br>--- CV#:" + str(cvids[line].get('data-hh-last-experience-id')) +
                  " ---<br> \n\n\n")
    cv_file.write(str(cvs[line]))

    cv_file.close()

hh_file.close()

