from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#FF2442"
GREEN = "#6ECB63"
BEIGE = "#FFEDDA"
ORANGE = "#FFB830"
BLUE = "#3DB2FF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 
def start_timer():
    pass

def reset_timer():
    pass

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
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=BEIGE, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_label = Label(text=CHECK_MARK, fg=GREEN, bg=BEIGE)
check_label.grid(row=3, column=1)

window.mainloop()
