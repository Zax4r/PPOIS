from Teacher import Teacher
from Student import Student
from Tests import Tests
from typing import List,Set,Tuple

class Administration:

    @staticmethod
    def add_student(students: List[Student]) -> List[Student]:
        print("Введите ФИО нового студента: ", end="")
        full_name = input()
        students.append(Student(full_name=full_name))
        return students

    @staticmethod
    def add_teacher(teachers: List[Teacher]) -> List[Teacher]:
        print("Введите ФИО нового преподавателя: ", end="")
        full_name = input()
        print("Введите предмет нового преподавателя: ", end="")
        subj = input()
        teachers.append(Teacher(full_name=full_name,subj=subj))
        return teachers

    @staticmethod
    def add_test(tests: List[Tests],subjects: Set[str]) -> Tuple[List[Tests],Set[str]]:
        print("Введите предмет нового теста: ", end="")
        subject = input()
        if subject not in subjects:
            subjects.add(subject)
            tests[subject] = []

        print("Введите название нового теста: ", end="")
        name = input()

        print("Введите количество вопросов в тесте: ", end="")
        while True:
            try:
                size = int(input())
                if size <= 0:
                    print("Положительное число!!")
                else:
                    break
            except ValueError:
                print("Должно быть число!!")

        tests[subject].append(Tests(subject, size, name))
        return tests,subjects