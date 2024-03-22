# my_list = [1,2,3,4,5,6,-5,-8]
# spisok = list(filter(lambda x: x> 0, my_list))
# print(spisok)

# words = ["ggh",'fghj',"ertyuio"]
# print(list(map(len, words)))

# func = lambda x,y: x*y
# res = func(3,5)
# print(res)

class Person:
    "ghjkl"
    weight = 65
    salary = 1000
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    @classmethod
    def validate(cls, arg: int):
        return cls.MIN_NUMBER <= arg <= cls.MAX_NUMBER

    def __new__(cls, *args, **kwargs):
        # print("вызов __new__" + str(cls))
        return super().__new__(cls)

    def __init__(self, name: str, surname: str, cvalif=1) -> None:
        # print("Вызов init" + str(self))
        self.name = name
        self.surname = surname
        self.cvalif = cvalif



#     def __del__(self):
#         print("Удаление экземпляра: ", str(self))

    def all_info(self):
        # print(str(self))
        return f"name - {self.name}, surname - {self.surname}, cvalification - \
            {self.cvalif}"


print(Person.validate(6))

person1 = Person(name="Klava", surname="Baboyan")
# print(person1.all_info())

# person2 = Person(name="vika", surname="Pak", cvalif=9)
# print(person2.all_info())

# print(person2.__dict__)

# print(hasattr(Person, "all_info"))


# setattr(Person, "weight", 62)
# # print(getattr(Person, "salary", False))
# # del Person.salary
# # print(getattr(Person, "salary", False))
# # print(hasattr(person2, "weight"))
# # print(person2.__dict__)
# # print(person2.__doc__)
# print(hasattr(person2, "weight"))

# del Person.weight
# print(getattr(Person, "weight", False))


# hasattr(person1.all_info, )

class DataBase:
    __inistance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inistance is None:
            cls.__inistance = super().__new__(cls)
            return cls.__inistance

    def __del__(self):
        DataBase.__inistance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БДЖ {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие ссоединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"записть в БД {data}")


db = DataBase("root", "1234", 30)
db2 = DataBase("root2", "5678", 80)
# print(id(db), id(db2))

db.connect()
# db2.connect()