from turtle import Turtle, Screen
import numpy as np
import random

screen = Screen()
screen.setup(1000, 1000)

class SnakeElement(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.right(-90)
        self.speed(0)

    def move_forwards(self):
        self.forward(20)

    def press_a(self):
        orientation = self.heading()
        if orientation == 90:
            self.left(90)
        if orientation == 270:
            self.right(90)
        else:
            pass

    def press_s(self):
        orientation = self.heading()
        if orientation == 180:
            self.left(90)
        if orientation == 0:
            self.right(90)
        else:
            pass

    def press_d(self):
        orientation = self.heading()
        if orientation == 90:
            self.right(90)
        if orientation == 270:
            self.left(90)
        else:
            pass

    def press_w(self):
        orientation = self.heading()
        if orientation == 0:
            self.left(90)
        if orientation == 180:
            self.right(90)
        else:
            pass

class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.new_location()

    def new_location(self):
        self.x = random.randrange(-screen.window_width() // 2, screen.window_width() // 2, 20)
        self.y = random.randrange(-screen.window_height() // 2, screen.window_height() // 2, 20)
        self.goto(self.x, self.y)

def detect_collision(snake):
    pos = []
    for i in snake:
        pos.append(i.pos())
    for i in pos:
        if pos.count(i)> 1:
            print("collision")
            return True
    return False








# Create a list to represent the snake
snake = [SnakeElement(), SnakeElement(), SnakeElement(), SnakeElement(), SnakeElement(),SnakeElement()]
snake[1].goto(0, -20)
snake[2].goto(0, -40)
snake[3].goto(0, -60)
snake[4].goto(0, -80)
snake[5].goto(0, -100)

dot = Dot()

screen.listen()

game_on = True
while game_on == True:
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(snake[i - 1].pos())

    snake[0].move_forwards()
    if detect_collision(snake):
        game_on = False
        screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color:")

    if abs(snake[0].xcor() - dot.xcor()) < 10 and abs(snake[0].ycor() - dot.ycor()) < 10:
        dot.new_location()
        new_element = SnakeElement()
        new_element.goto(snake[0].pos())
        new_element.setheading(snake[0].heading())
        new_element.forward(20)
        snake.insert(0, new_element)



    # Attach key events to the entire snake
    screen.onkey(key="a", fun=snake[0].press_a)
    screen.onkey(key="s", fun=snake[0].press_s)
    screen.onkey(key="w", fun=snake[0].press_w)
    screen.onkey(key="d", fun=snake[0].press_d)

    screen.update()
