from turtle import Turtle, Screen
import numpy as np
import random
screen = Screen()

# t = Turtle()
# t.width(2)
# t.shape("turtle")
# t.color("red")
# t.forward(100)
# t.right(45)
# t.forward(100)

'''draw polygons'''
# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]
# t = Turtle()
# t.shape("triangle")
# for i in np.arange(3,20):
#     t.color(random.choice(colors))
#     for j in range(i):
#         t.forward(100)
#         t.right(360/i)


'''random walk'''

# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]
# t = Turtle()
#
# direction = [90,180,270,360]
# t.speed(0)
# while True:
#     t.forward(100)
#     t.pensize(10)
#     t.right(random.choice(direction))

'''tuple'''
# my_tuple = (1,3,5)
# my_tuple[1]
# list(my_tuple)
#
# # colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]
# t = Turtle()
# # t.colormode(255)


'''rgb color'''
# t = Turtle()
# # t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
#     return (r/255,g/255,b/255)
#
#
# direction = [90,180,270,360]
# t.speed(0)
# while True:
#     t.forward(100)
#     t.pensize(10)
#     t.color(random_color())
#     t.right(random.choice(direction))

"""spirograph"""

# t = Turtle()
# # t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
#     return (r/255,g/255,b/255)
#
#
# direction = [90,180,270,360]
# t.speed(10)
#
# def spiral():
#     for i in np.arange(360):
#         t.forward(1)
#         t.left(1)

"""spirograph"""

# t = Turtle()
# # t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
#     return (r/255,g/255,b/255)
#
#
# direction = [90,180,270,360]
# t.speed(10)
#
# for i in np.arange(1,360,10):
#     t.left(i)
#     t.circle(100)
#

"""damien hirst color palette"""


# t = Turtle()
# # t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
#     return (r/255,g/255,b/255)
#
#
# direction = [90,180,270,360]
# t.speed(10)
# t.hideturtle()
# for i in np.arange(10):
#     for j in np.arange(10):
#         t.color(random_color())
#         t.begin_fill()  # Begin filling
#         t.dot(10)  # Draw a circle with a radius of 100
#         t.end_fill()
#         t.penup()
#         t.forward(50)
#         t.pendown()
#     t.penup()
#     t.backward(500)
#     t.left(90)
#     t.forward(50)
#     t.right(90)
#     t.pendown()


'''bind keystroke to code'''
# t = Turtle()
#
#
# def move_forwards():
#     t.forward(10)
#
#
#
# screen.listen() # bind keystroke to code
# screen.onkey(key = "space", fun = move_forwards) # when passing a function not to use



"""etch a sketch"""

# t = Turtle()
#
#
# def move_forwards():
#     t.forward(10)
#
# def move_backwards():
#     t.backward(10)
#
# def move_left():
#     t.left(10)
#
# def move_right():
#     t.right(10)
#
#
#
#
#
# screen.listen() # bind keystroke to code
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = move_left)
# screen.onkey(key = "d", fun = move_right)

"""turtle race"""

t = Turtle()
screen.setup(500,400)

user_bet = screen.textinput(title = "make your bet", prompt = "which turtle will win the race? Enter a color:" )

# initialize and set position

y_corr = [-200, -100 , 0, 100, 200]

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]

class MyTurtle(Turtle):
    def __init__(self, offset):
        super().__init__() # call the base class constructor
        self.color(random.choice(colors))
        self.penup()
        self.goto(x =-100, y = offset)
        self.total_distance = 0
        # self.pendown()

    def move(self):
        displacement = random.randint(0,20)
        self.total_distance += displacement
        self.forward(displacement)
        return self.total_distance





tim1  = MyTurtle(-200)
tim2  = MyTurtle(-100)
tim3  = MyTurtle(0)
tim4  = MyTurtle(100)
tim5  = MyTurtle(200)
x = 0

finish_line = Turtle()
finish_line.penup()
finish_line.forward(500)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(200)
finish_line.backward(400)
finish_line.hideturtle()

list_participants = [tim1, tim2, tim3, tim4, tim5]
a = "start"
while a !="finish":
    for i in range(5):
        x = list_participants[i].move()
        print(f"{i}-{x}")
        if x>=600:
            print(f"Tim{i} wins")
            a = "finish"
            break































screen.exitonclick()

