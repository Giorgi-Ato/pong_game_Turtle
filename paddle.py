from turtle import Turtle

WIDTH = 1
HEIGHT = 5


class Paddle(Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.shapesize(HEIGHT, WIDTH)
        self.goto(x_cord, y_cord)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
