import time
from turtle import Turtle, Screen
# from right_paddle import Paddle
from my_paddles import Paddle
from ball import Ball
from score_board import Score
screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

c = 0.1
on = True
while on:
    time.sleep(ball.increse_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.restart()
        score.left_user_score()

    if ball.xcor() < -380:
        ball.restart()
        score.right_user_score()





screen.exitonclick()