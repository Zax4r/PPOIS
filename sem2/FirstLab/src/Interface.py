from Student import Student
from Teacher import Teacher
from Tests import Tests
from Feedback import Feedback
from Administation import Administration
from MyOwnException import MyOwnException
from typing import List,Set,Tuple

class Interface:
    def __init__(self):
        self.__feedback = Feedback() 
        self.__subjects = set()
        self.__students = []
        self.__teachers = [] 
        self.__tests = {}

    @property
    def subjects(self) -> Set(str):
        return self.__subjects

    @property
    def teachers(self) -> List[Teacher]:
        return self.__teachers

    @property
    def tests(self) -> List[Tests]:
        return self.__tests

    def __validate_input(self, lower_boundary: int, upper_boundary: int) -> int:
        while True:
            try:
                choice = int(input())
                if lower_boundary <= choice <= upper_boundary:
                    return choice
                else:
                    print("Такого пункта в меню нет, напишите правильно!")
            except ValueError:
                print("Напишите ЦИФРУ пункта меню!")

    def show_menu(self):
        print("Выберите пункт меню:\n\
              1. Операция проведения тестирования.\n\
              2. Операция выставления оценок.\n\
              3. Операция анализа результатов.\n\
              4. Операция обратной связи.\n\
              5. Операция администрирования системы.\n\
              6. Просмотреть статистику учащихся\n\
              0. Выход")

    def menu(self):
        self.show_menu()
        choice = self.__validate_input(0, 6)
        
        match choice:

            case 0:
                raise MyOwnException("Выход из программы")
            case 1:
                self.testing()
            case 2:
                self.marking()
            case 3:
                self.analytics()
            case 4:
                self.feedback_operation()
            case 5:
                self.administration_operation()
            case 6:
                self.show_stats()

    def show_stats(self):
        for student in self.__students:
            student.show_stats()

    def administration_operation(self):
        print("Выберите пункт администрирования:\n\
              1. Добавить студента.\n\
              2. Добавить преподавателя.\n\
              3. Добавить тест.\n")
        
        choice = self.__validate_input(1, 3)
        match choice:
            case 1:
                self.__students = Administration.add_student(self.__students)
            case 2:
                self.__teachers = Administration.add_teacher(self.__teachers)
            case 3:
                self.__tests,self.__subjects = Administration.add_test(self.__tests,self.__subjects)

    def testing(self):
        if not self.__tests:
            print("Нет тестов!!")
            return
        
        print("Выберите предмет теста (введите название): ")
        subjects_list = list(self.__subjects)
        for index, subj in enumerate(subjects_list, start=1):
            print(f"{index}. {subj}")
        
        choice = self.__validate_input(1, len(subjects_list))

        subject_input = subjects_list[choice - 1]
        tests_subj = self.__tests[subject_input]
        
        print("Выберите тест: ")
        for index, test in enumerate(tests_subj, start=1):
            print(f"{index}. {test.name} ({test.size})")
        
        choice_test = self.__validate_input(1, len(tests_subj))
        tests_subj[choice_test - 1].start_test(self.__students)

    def marking(self):
        for student in self.__students:
            student.marking()

    def analytics(self):
        for student in self.__students:
            student.analytics()
        
    def feedback_operation(self):
        print("Выберите пункт меню:\n\
              1. Оставить отзыв.\n\
              2. Посмотреть отзывы.")
        
        choice = self.__validate_input(1, 2)

        if choice == 1:
            self.__feedback.add_review()
        elif choice == 2:
            self.__feedback.show_reviews()