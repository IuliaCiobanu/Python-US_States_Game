from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color = "white"
        self.setpos(-100, 280)
        self.score = 0
        self.write(f"STATES = {self.score} out of 50")

    def add_points(self):
        self.score += 1
        self.clear()
        self.write(f"STATES = {self.score} out of 50")

