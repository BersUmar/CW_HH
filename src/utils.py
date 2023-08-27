from src.connect import Connector
from src.job_vacancy import HHVac, SJVac


def sort(vacancy):
    return sorted(vacancy)

def top(vacancy, count):
    return list(sorted(vacancy, reverse=True)[:count])

def get_hh_vacancy(connector: Connector):
    vacancies = [
        HHVac(
            title=vacancy['name'],
            link=vacancy['alternate_url'],
            description=vacancy['snippet'],
            salary=vacancy['salary']['from'] if vacancy['salary'] else None)
        for vacancy in connector.select({})]
    return vacancies

def get_sj_vacancy(connect):
    vacancies = [
        SJVac(
            title=vacancy['profession'],
            link=vacancy['link'],
            description=vacancy['candidat'],
            salary=vacancy['payment_from'])
        for vacancy in connect.select({})]
    return vacancies
