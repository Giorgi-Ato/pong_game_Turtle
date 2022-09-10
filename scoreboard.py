from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 50, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    # def score(self):
    #     self.clear()
    #     self.write(f'{self.l_score} : {self.r_score}', align=ALIGN, font=FONT)

    def add_r_score(self):
        self.r_score += 1

    def add_l_score(self):
        self.l_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

