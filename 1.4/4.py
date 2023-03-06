import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for el in data:
            tmp = dict(zip(self.FIELDS, tuple(el.split(' '))))
            self.lst_data.append(tmp)

    def select(self, a, b):
        try:
            return self.lst_data[a:b + 1]
        except:
            return self.lst_data


db = DataBase()
db.insert(lst_in)
