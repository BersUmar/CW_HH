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
        if not os.path.exists(self.__file):
            with open(self.__file, 'w', encoding='UTF-8') as f:
                print(f)

