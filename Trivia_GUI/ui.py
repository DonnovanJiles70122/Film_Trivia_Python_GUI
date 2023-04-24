from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WRONG_COLOR = '#FF6969'
RIGHT_COLOR = '#C7E9B0'

class QuizIntergace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Film Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=200, height=200, bg=THEME_COLOR, highlightthickness=0)
        self.film_image = PhotoImage(file="images/film_logo.png")
        self.canvas.create_image(100, 100, image=self.film_image)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.title_label = Label(text="Film Trivia Quiz", fg="Black", bg=THEME_COLOR, font=('Arial', 18, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2)
        

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=20)
        self.score_label.grid(row=2, column=1)

        self.canvas_textbox = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas_textbox.create_text(
            150,
            125, 
            width=280,
            text="Some Question Text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas_textbox.grid(row=3, column=0, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true_2.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=4, column=0)

        false_imgae = PhotoImage(file="images/false_2.png")
        self.false_button = Button(image=false_imgae, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(row=4, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas_textbox.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas_textbox.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas_textbox.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_textbox.config(bg=RIGHT_COLOR)
        else:
            self.canvas_textbox.config(bg=WRONG_COLOR)
        self.window.after(1000, self.get_next_question)

