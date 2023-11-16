import turtle as t

# Set up the turtle screen
screen = t.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Create a turtle object
mona_lisa = t.Turtle()
mona_lisa.speed(0)  # Fastest drawing speed

# Function to draw a colored rectangle
def draw_rectangle(color, width, height):
    mona_lisa.fillcolor(color)
    mona_lisa.begin_fill()
    for _ in range(2):
        mona_lisa.forward(width)
        mona_lisa.right(90)
        mona_lisa.forward(height)
        mona_lisa.right(90)
    mona_lisa.end_fill()

# Draw a simplified Mona Lisa-like image
draw_rectangle("khaki", 300, 400)  # Face background
draw_rectangle("rosybrown", 100, 200)  # Left eye background
draw_rectangle("rosybrown", 100, 200)  # Right eye background
draw_rectangle("black", 20, 100)  # Left eye
draw_rectangle("black", 20, 100)  # Right eye
draw_rectangle("saddlebrown", 100, 20)  # Eyebrows
draw_rectangle("red", 150, 20)  # Lips
draw_rectangle("black", 100, 300)  # Hair
draw_rectangle("white", 30, 40)  # Left highlight
draw_rectangle("white", 30, 40)  # Right highlight

# Hide the turtle
mona_lisa.hideturtle()

# Close the turtle graphics window on click
screen.exitonclick()
