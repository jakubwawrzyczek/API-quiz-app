from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzzz')
        self.window.configure(pady=20, padx=20, bg=THEME_COLOR)

        # score
        self.score_lbl = Label(text='score: 0', bg=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1)

        # canvas
        self.main_canv = Canvas(width=300, height=250, bg='white')
        self.question_text = self.main_canv.create_text(
            150,
            125,
            width=290,
            text='Hello',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'))
        self.main_canv.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.true_btn = Button(image=true_image, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=false_image, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.main_canv.itemconfig(self.question_text, text=q_text)
