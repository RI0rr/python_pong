from turtle import Turtle

class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.start_pos = pos
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
    def go_up(self):
        self.sety(self.ycor() + 20)
    def go_down(self):
        self.sety(self.ycor() - 20)
    def restart(self):
        self.goto(self.start_pos)
    start_pos = (0, 0)