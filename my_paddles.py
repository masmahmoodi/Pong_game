from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)





    def go_up(self):
        x_side = self.xcor()
        y_side = self.ycor()+20
        self.goto(x_side,y_side)

    def go_down(self):
        x_side = self.xcor()
        y_side = self.ycor()-20
        self.goto(x_side,y_side)


