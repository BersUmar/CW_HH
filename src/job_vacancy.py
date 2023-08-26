class Vacancy:
    __slots__ = {"title", "link", "description", "salary"}

    def __init__(self, title, link, description, salary):
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return f'Vacancy: title="{self.title}", link="{self.link}", description="{self.description}", salary="{self.salary}"'

    def __str__(self):
        return self.title

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        if other.salary is None:
            return False
        if self.salary is None:
            return True

        return self.salary < other.salary

class HHVac(Vacancy):
    def __str__(self):
        return f"HeadHunter: {self.title}, salary: {self.salary}"

class SJVac(Vacancy):
    def __str__(self):
        return f"SuperJOB: {self.title}, salary: {self.salary}"
