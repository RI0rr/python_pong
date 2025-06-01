from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(str(self.l_score) + " - " + str(self.r_score), move=False, align="center", font=("Arial", 20, "normal"))

    def update(self):
        self.clear()
        self.write(str(self.l_score) + " - " + str(self.r_score), move=False, align="center",font=("Arial", 20, "normal"))

    l_score = 0
    r_score = 0