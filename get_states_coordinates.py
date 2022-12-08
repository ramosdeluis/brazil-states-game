from turtle import Turtle


class GetCoor(Turtle):
    def __init__(self):
        super(GetCoor, self).__init__()
        self.shape('circle')
        self.penup()

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-10)

    def move_left(self):
        self.goto(self.xcor()-10, self.ycor())

    def move_right(self):
        self.goto(self.xcor()+10, self.ycor())
