class Marks:
    def __init__(self):
        self.__subjects = set()
        self.__last_index = 0  # next test that should be marked
        self.__test_results = []  #[(subj,points_claimed,points_possible)]
        self.__marks = {}  #[subj]:[list of marks]
        self.__analytics = {} #[subj]:[list of analytic results]
        self.__undone__marks = []  #[(subj,mark)]

    def add_test_results(self, subject: str, points_claimed: int, points_possible: int):
        self.__test_results.append((subject, points_claimed, points_possible))
        if subject not in self.__subjects:
            self.__subjects.add(subject)
            self.__marks[subject] = []
            self.__analytics[subject] = []

    def marking(self):
        try:
            self.__test_results[self.__last_index]
        except IndexError:
            print("Нет необработанных результатов теста!")
            return

        for i in range(self.__last_index, len(self.__test_results)):
            subject, points_claimed, points_possible = self.__test_results[i]
            mark = int((points_claimed / points_possible) * 10 + 0.5)
            self.__marks[subject].append(mark)
            self.__undone__marks.append((subject, mark))
        
        self.__last_index = len(self.__test_results) + 1

    def analytic(self):
        if not len(self.__undone__marks):
            print("Нет необработанных оценок!")
            return

        for subject, mark in self.__undone__marks:
            self.__analytics[subject].append("Зачёт!" if mark > 3 else "Не сдал!")
        
        self.__undone__marks.clear()

    def show_stats(self):
        print(f"Результаты тестов: {self.__test_results}\n\
                Оценки: {self.__marks}\n\
                Аналитика: {self.__analytics}", end="\n\n")