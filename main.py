from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG GAME')
screen.tracer(0)

r_pddl = Paddle(350, 0)
l_pddl = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
# Right Paddle
screen.onkey(r_pddl.go_up, 'Up')
screen.onkey(r_pddl.go_down, 'Down')
# Left Paddle
screen.onkey(l_pddl.go_up, 'w')
screen.onkey(l_pddl.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()

    # Detect collision with Paddle
    if ball.distance(r_pddl) < 50 and ball.xcor() > 320 or ball.distance(l_pddl) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R Paddle misses
    if ball.xcor() > 380:
        score.add_l_score()
        score.update_scoreboard()
        ball.restart_moving_position()

    # Detect L Paddle misses
    if ball.xcor() < -380:
        score.add_r_score()
        score.update_scoreboard()
        ball.restart_moving_position()

screen.exitonclick()
