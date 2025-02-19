class Review:
    def __init__(self, author: str, text_review: str):
        self.__author = author
        self.__text_review = text_review

    def show_review(self):
        print(f"Отзыв от {self.__author}: {self.__text_review}")