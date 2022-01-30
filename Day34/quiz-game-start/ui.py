from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questiontext = self.canvas.create_text(150, 125, width=280, text="Some text", fill="black", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Creating widgets
        cross_img = PhotoImage(file="./images/wrong.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.check_answer_false)
        self.cross_button.grid(row=2, column=1)

        right_img = PhotoImage(file="./images/right.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.check_answer_true)
        self.right_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            ques = self.quiz.next_question()
            #print(ques)
            self.canvas.itemconfig(self.questiontext, text=ques)
        else:
            self.canvas.itemconfig(self.questiontext, text="You have reached end of questions.")
            self.cross_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

