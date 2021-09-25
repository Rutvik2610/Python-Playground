from tkinter import *
import pandas
import random

CURRENT_CARD = {}
BACKGROUND_COLOR = "#B1DDC6"

# ----------------------Load Data--------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    dict_of_words = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")
    dict_of_words = data.to_dict(orient="records")


# ----------------------Next Card------------------------
def next_card():
    global flip_timer, CURRENT_CARD
    window.after_cancel(flip_timer)
    if len(dict_of_words) == 0:
        return
    CURRENT_CARD = random.choice(dict_of_words)
    canvas.itemconfig(card_image, image=front_png)
    canvas.itemconfig(language_title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_CARD["French"], fill="black")
    flip_timer = window.after(3000, answer_card, CURRENT_CARD)


def answer_card(card):
    canvas.itemconfig(card_image, image=back_png)
    canvas.itemconfig(language_title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")


# --------------------Saving Progress---------------------
def answer_known():
    if len(dict_of_words) == 0:
        canvas.itemconfig(language_title_text, text="Congratulations!!!", fill="black", font=("Ariel", 30, "italic"))
        canvas.itemconfig(word_text, text="You've memorized all the words", fill="black", font=("Ariel", 30, "bold"))
        window.after_cancel(flip_timer)
        return

    dict_of_words.remove(CURRENT_CARD)
    df = pandas.DataFrame(dict_of_words)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, answer_card, CURRENT_CARD)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_png = PhotoImage(file="images/card_front.png")
back_png = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_png)
language_title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_png = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_png, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_png = PhotoImage(file="images/right.png")
right_button = Button(image=right_png, highlightthickness=0, command=answer_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
