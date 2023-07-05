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

        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.main_canv.config(bg='white')
        self.score_lbl.config(text=f'score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.main_canv.itemconfig(self.question_text, text=q_text)
        else:
            self.main_canv.itemconfig(self.question_text, text='You have reached to the end of the quiz!\n'
                                                               f'Your final score is {self.quiz.score} out of the 10, '
                                                               f'good job!')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer='True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer='False'))

    def give_feedback(self, is_right):
        if is_right:
            self.main_canv.config(bg='green')
        else:
            self.main_canv.config(bg='red')
        self.window.after(300, self.get_next_question)
