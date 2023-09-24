
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
left_player = Paddle((-350, 0))
right_player = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")
#screen.onkey(ball.restart, "space")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    
    

screen.exitonclick()