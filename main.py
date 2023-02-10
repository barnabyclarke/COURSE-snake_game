from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
AREA = 290

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.score()

    # Detect collision with food
    if snake.head.distance(food) < 5:
        food.refresh()
        snake.extend()
        scoreboard.new_score()

    # Detect collision with wall
    if snake.head.xcor() > AREA or snake.head.xcor() < -AREA or snake.head.ycor() > AREA or snake.head.ycor() < -AREA:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    snake.move()

screen.exitonclick()
