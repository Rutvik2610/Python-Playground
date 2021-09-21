from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#FF2442"
GREEN = "#6ECB63"
BEIGE = "#FFEDDA"
ORANGE = "#FFB830"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    start_button.config(state="normal")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button.config(state="disabled")
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    global reps
    reps = 0
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work")
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=ORANGE)


def pause_timer():
    count = canvas.itemcget(timer_text, "text").split(":")
    count_min = int(count[0])
    count_sec = int(count[1])
    total_sec = count_sec + count_min * 60

    if start_button["state"] == "disabled":
        window.after_cancel(timer)
        start_button.config(state="normal")

    else:
        start_button.config(state="disabled")
        count_down(total_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += CHECK_MARK
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

canvas = Canvas(width=200, height=234, bg=BEIGE, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=BEIGE, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", fg=RED, command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

pause_button = Button(text="Pause", fg=RED, command=pause_timer, highlightthickness=0)
pause_button.grid(row=2, column=1)

reset_button = Button(text="Reset", fg=RED, command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=BEIGE, font=(FONT_NAME, 15, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()
