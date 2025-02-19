from Review import Review

class Feedback:
    def __init__(self):
        self.__reviews = []

    def add_review(self):
        print("Введите ФИО автора отзыва: ")
        author = input()
        print("Введите текст отзыва: ")
        text_review = input()
        self.__reviews.append(Review(author=author,text_review=text_review))

    def show_reviews(self):
        for review in self.__reviews:
            review.show_review()