from Marks import Marks
from random import randint

class Student:
    def __init__(self, full_name: str):
        self.__marks = Marks()  
        self.__full_name = full_name  

    def testing(self, points_possible: int, subject: str):
        answer = self.think(points_possible)
        self.__marks.add_test_results(subject, answer, points_possible)

    def marking(self):
        self.__marks.marking()

    def analytics(self):
        self.__marks.analytic()

    def show_stats(self):
        print(f"Статистика студента {self.__full_name}:")
        self.__marks.show_stats()

    def think(self, points_possible: int) -> int:
        return randint(1, points_possible)