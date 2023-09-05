import json

from src.connect import Connector
from src.engine import HH, Superjob
from src.utils import sort, get_hh_vacancy, get_sj_vacancy, top


def main():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    # keyword = 'python'
    hh_engine = HH(keyword)
    sj_engine = Superjob(keyword)
    hh_connector = Connector("vacancy_hh.json")
    sj_connector = Connector("vacancy_sj.json")
    hh_vacancies = hh_engine.get_request().json()["items"]
    sj_vacancies = sj_engine.get_request().json()["objects"]
    for vacancy in hh_vacancies:
        hh_connector.insert(vacancy)
    for vacancy in sj_vacancies:
        sj_connector.insert(vacancy)

    while True:
        command = input('sort/top: ')
        if command == 'sort':
            hh_vacancies = get_hh_vacancy(hh_connector)
            sj_vacancies = get_sj_vacancy(sj_connector)
            sorted_vacancies = sort(hh_vacancies + sj_vacancies)
            for vacancy in sorted_vacancies:
                print(vacancy)
        elif command == 'top':
            hh_vacancies = get_hh_vacancy(hh_connector)
            sj_vacancies = get_sj_vacancy(sj_connector)
            top_count = int(input('введите количество необходимых вакансий: '))
            sorted_vacancies = top(hh_vacancies + sj_vacancies, top_count)
            for vacancy in sorted_vacancies:
                print(vacancy)
        elif command == "exit":
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
