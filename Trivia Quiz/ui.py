from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Creating the window
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating Score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        # Creating Canvas
        self.canvas = Canvas(width=300, height=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     150,
                                                     width=280,
                                                     text="Question will be displayed here",
                                                     font=("Ariel", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=self.pressed_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text,
                                   text=f"Your Final Score is:\n{self.quiz.score}/{self.quiz.question_number}",
                                   font=("Ariel", 30, "bold"))

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="medium spring green")
        else:
            self.canvas.config(bg="tomato")
        self.window.after(1000, self.get_next_question)
