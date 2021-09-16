import turtle

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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name:")

screen.exitonclick()
