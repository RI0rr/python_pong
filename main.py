from cgitb import reset
from itertools import filterfalse
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

speed_increase = 1.5

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Players
l_player = Player((350, 0))
r_player = Player((-350, 0))
players = [l_player, r_player]

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

screen.listen()

# Right input
screen.onkey(r_player.go_up, "Up")
screen.onkey(r_player.go_down, "Down")

# Left input
screen.onkey(l_player.go_up, "w")
screen.onkey(l_player.go_down, "s")

game_over = False

def restart():
    scoreboard.update()
    ball.restart()
    for paddle in players:
        paddle.restart()

while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Check collision with walls
    if ball.xcor() >= 380:
        scoreboard.l_score += 1
        restart()

    if ball.xcor() <= -380:
        scoreboard.r_score += 1
        restart()

    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.y_dir *= -1
        ball.speed += speed_increase

    # Check collision with players
    for player in players:
        if ball.distance(player.xcor(), player.ycor()) <= 25:
            print("Collision with player detected")
            ball.x_dir *= -1
            ball.speed += speed_increase

screen.exitonclick()
