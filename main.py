import json

from src.connect import Connector
from src.engine import HH, Superjob
from src.utils import sort, get_hh_vacancy, get_sj_vacancy, top


def main():

    # keyword = input("Введите ключевое слово для поиска вакансий: ")
    keyword = 'python'
    hh_engine = HH(keyword)
    sj_engine = Superjob(keyword)
    hh_connector = Connector("vacancy_hh.json")
    sj_connector = Connector("vacancy_sj.json")
    page = 0
    hh_pages = 1
    hh_close = False
    more = True
    while True:
        if page < hh_pages:
            hh_engine.params['page'] = page
            page += 1
            hh_vacancies = json.dumps(hh_engine.get_request())
            hh_pages = hh_vacancies['pages']
            hh_items = hh_vacancies['items']
            hh_connector.insert(hh_items)
        else:
            hh_close = True

        if more:
            sj_engine.params['page'] = sj_engine.params['page'] + 1
            sj_vacancies = json.dumps(sj_engine.get_request())
            sj_items = sj_vacancies['objects']
            more = sj_vacancies['more']
            sj_connector.insert(sj_items)

        if hh_close and not more:
            break

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
            all_vacancies = hh_vacancies + sj_vacancies
            top_count = int(input('введите количество необходимых вакансий: '))
            top_vacancies = top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)
        else:
            print("Некорректная команда, повторите попытку: ")
        continue_run = input("хотите продолжить работу с программой? (y/n)")
        if continue_run == 'n':
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
