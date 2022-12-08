from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super(Board, self).__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(235, 300)
        self.write_board()

    def make_point(self):
        self.score += 1
        self.clear()
        self.write_board()

    def write_board(self):
        self.write(f"Score: {self.score}/27", move=False, align='center', font=('Arial', 35, 'normal'))

    def end_game(self):
        self.home()
        self.write(f"You Win The Game!", move=False, align='center', font=('Arial', 50, 'normal'))
