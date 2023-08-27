import json
import os.path


class Connector:
    def __init__(self, file_path):
        self.__file = file_path
        self.__connect()

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value
        self.__connect()

    def __connect(self):
        """проверка существования файла json"""
        if not os.path.exists(self.__file):
            with open(self.__file, 'w', encoding='UTF-8') as f:
                f.write(json.dumps([]))

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__file, 'r') as file:
            file_data = json.load(file)
        file_data.append(data)
        with open(self.__file, 'w') as file:
            json.dump(file_data, file)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(self.__file, 'r') as file:
            file_data = json.load(file)

        if not query:
            return file_data

        result = []
        for entry in file_data:
            if all(entry.get(key) == value for key, value in query.items()):
                result.append(entry)
        return result
