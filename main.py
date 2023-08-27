from src.connect import Connector
from src.engine import HH, Superjob
from src.utils import sort, get_hh_vacancy, get_sj_vacancy, top


def main():
    # keyword = input("Введите ключевое слово для поиска вакансий: ")
    keyword = 'python'
    hh_engine = HH(keyword)
    sj_engine = Superjob(keyword)
    connector = Connector("vacancy.json")
    # Получить вакансии из апи hh и sj
    connector.insert(get_hh_vacancy(hh_engine.get_request()))
    connector.insert(get_sj_vacancy(sj_engine.get_request()))

    while True:
        command = input("Введите команду (sort, top, search): ")
        if command == "sort":
            sort(connector)
        elif command == "top":
            top(connector)
        else:
            print("Некорректная команда. Попробуйте ещё раз.")
        continue_running = input("Хотите продолжить работу с программой? (yes/no): ")
        if continue_running.lower() == "no":
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
