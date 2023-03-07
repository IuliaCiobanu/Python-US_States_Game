# import the time module
import time
from turtle import Turtle

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color = "red"
        self.setpos(200, 280)
        self.t = 60
        self.countdown()

# define the countdown func.
    def countdown(self):
        while self.t:
            mins, secs = divmod(self.t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.t -= 1

        print('GAME OVER')


# input time in seconds
# t = input("Enter the time in seconds: ")

# function call
