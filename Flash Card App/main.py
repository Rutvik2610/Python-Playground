from tkinter import *
import pandas

data = pandas.read_csv("data/french_words.csv")
df = pandas.DataFrame(data)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Images
front_png = PhotoImage(file="images/card_front.png")
back_png = PhotoImage(file="images/card_back.png")
right_png = PhotoImage(file="images/right.png")
wrong_png = PhotoImage(file="images/wrong.png")
canvas.create_image(400, 263, image=front_png)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=df.French[0], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_png, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_png, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
