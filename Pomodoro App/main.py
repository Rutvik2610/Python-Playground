from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#FF2442"
BEIGE = "#FFEDDA"
ORANGE = "#FFB830"
BLUE = "#3DB2FF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
