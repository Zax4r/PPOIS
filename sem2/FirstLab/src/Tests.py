from Student import Student
from typing import List

class Tests:
    def __init__(self, subject: str, size: int, name: str):
        self.__size = size 
        self.__subject = subject 
        self.__name = name  

    @property
    def size(self) -> int:
        return self.__size
    
    @property
    def name(self) -> str:
        return self.__name

    def start_test(self, students: List[Student]):
        for student in students:
            student.testing(self.__size, self.__subject)
