class Teacher:
    def __init__(self,full_name: str, subj: str):
        self.__full_name = full_name
        self.__subj = subj

    def __str__(self):
        return f"Преподователь {self.__full_name}, ведущий предмет {self.__subj}"