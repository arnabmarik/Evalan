import turtle as t
import pandas as pd

# Set up the Turtle screen
screen = t.Screen()
screen.title("U.S. States Game")

# Read the data from the CSV file
data = pd.read_csv("50_states.csv")

# Initialize variables
total_correct = 0

while total_correct < 50:  # Check if the user has guessed all 50 states
    answer_state = screen.textinput(title=f"{total_correct}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break  # Exit the game if the user enters "Exit"

    # Check if the guessed state is in the list of states
    state_list_lower = data["state"].str.lower()

    if answer_state.lower() in state_list_lower.tolist():
        state_row = data[data["state_list_lower"] == answer_state.lower()]

        # Create a Turtle for displaying the state name
        turtle = t.Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(state_row['x']), int(state_row['y']))
        turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
        total_correct += 1

# Close the Turtle graphics window on click
screen.exitonclick()
