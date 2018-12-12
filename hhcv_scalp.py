import time
import os
from bs4 import BeautifulSoup


def cv_parse(hh_filename):

    hh_file = open("HHSaves\\" + hh_filename, 'rb')

    soup = BeautifulSoup(hh_file, 'html.parser')  # Просим BeautifulSoup "разобрать" полученную
    # страничку на элементы, создав объект soup

    cvs = soup.find_all(class_="resume-search-item__content-wrapper")
    cvids = soup.find_all(class_="bloko-toggle HH-Employer-VacancyResponse-Topic-ExperienceTrigger")

    # data-hh-last-experience-id

    for line in range(0, len(cvs)):
        cv_file = open("CVStore\\cv_" + str(cvids[line].get('data-hh-last-experience-id') + ".html"), 'w', encoding='utf-8')

        cv_file.write("\n\n\n <br>--- CV#:" + str(cvids[line].get('data-hh-last-experience-id')) +
                      " --- " + file_list[g] + "<br> \n\n\n")
        cv_file.write(str(cvs[line]))

        cv_file.close()

    hh_file.close()


def hhsave_getlist():
    file_getlist = os.walk("HHSaves\\")
    name_list = []
    for d in file_getlist:
        name_list.append(d[-1])
    return name_list


file_list = hhsave_getlist()
file_list = file_list[0]

for g in range(0, len(file_list)):
    print(file_list[g], "\n")
    cv_parse(file_list[g])
