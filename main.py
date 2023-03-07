import turtle
import pandas
from score import Score

screen = turtle.Screen()
screen.title("U.S. STATES GAME")

# INSERARE IMAGINE
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

start_score = Score()

data = pandas.read_csv("50_states.csv")
all_states_list = data.state.to_list()

your_correct_answers_list = []

while len(your_correct_answers_list) < 50:
    # #PROMPT POPUP BOX:
    user_answer = screen.textinput(title="Guess the State", prompt="What's another state's state_name?").title()
    print(user_answer)

    if user_answer=="Exit":
        missing_states = [item for item in all_states_list if item not in your_correct_answers_list]
        # missing_states = []
        # for item in all_states_list:
        #     if item not in your_correct_answers_list:
        #         missing_states.append(item)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if user_answer not in your_correct_answers_list:
        if user_answer in all_states_list:
            state_info = data[data.state == user_answer]
            state_x_coor = int(state_info.x)
            state_y_coor = int(state_info.y)

            object = turtle.Turtle()
            object.penup()
            object.hideturtle()
            object.goto(state_x_coor, state_y_coor)
            object.write(user_answer.title())
            your_score = start_score.add_points()
            your_correct_answers_list.append(user_answer)

# turtle.mainloop()