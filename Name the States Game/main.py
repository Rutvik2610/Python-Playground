import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic('blank_states_img.gif')

# To get the screen co-ordinates of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

dataset = pandas.read_csv("50_states.csv")
all_states = dataset.state.to_list()

correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to Learn")
        break

    if (answer_state in all_states) and (answer_state not in correct_guess):
        correct_guess.append(answer_state)
        state_data = dataset[dataset.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(answer_state)
