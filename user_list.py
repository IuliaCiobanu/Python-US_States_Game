from turtle import Turtle
from score import Score


class User_Guesses:
    def __init__(self, user_answer):
        self.list = []
        self.add_answers(user_answer)
        print(self.list)


    def add_answers(self, user_answer):
        self.list.append(user_answer)

    def check_repeted_answers(self, user_answer):
        for names in self.list:
            if self.list[name] == user_answer:
                return False
            # start_score = Score()
            # self.your_score = start_score.add_points()
