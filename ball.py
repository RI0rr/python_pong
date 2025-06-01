from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.width = 20
        self.height = 20
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.speed * self.x_dir
        new_y = self.ycor() + self.speed * self.y_dir
        self.goto(new_x, new_y)

    def restart(self):
        self.goto(0, 0)
        self.speed = 10
        self.x_dir = 1
        self.y_dir = 1

    speed = 10
    x_dir = 1
    y_dir = 1
