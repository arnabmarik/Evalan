import turtle as t
import pandas as pd


screen = t.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.bgpic(image)

t.shape("circle")


#
# def get_mouse_click_corr(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_corr)
#
# turtle.mainloop() # keeps the screen open

# answer_state = str(screen.textinput(title="guess the state", prompt="what's another state's name?"))
# total_correct = 0
# while True:
#     print(answer_state)
#     # check if it's a real state
#     data = pd.read_csv("50_states.csv")
#     state_list_lower = data["state"].str.lower()
#     data['date_list_lower'] = state_list_lower
#     print(data)
#     for i in state_list_lower:
#         if i.lower() == answer_state.lower():
#             state_row = data[data["date_list_lower"] == answer_state.lower()]
#             turtle = t.Turtle()
#             turtle.penup()
#             turtle.goto(int(state_row['x']), int(state_row['y']))
#             turtle.write(answer_state)
#             total_correct +=1
#     title = f"{total_correct}/50"
#     answer_state = str(screen.textinput(title=title, prompt="what's another state's name?"))

total_correct = 0
guessed_states = []
while total_correct<50:
    # convert to title case
    answer_state = screen.textinput(title=f"{total_correct}/50", prompt="What's another state's name?").title()
    # check if it's a real state
    data = pd.read_csv("50_states.csv")
    if answer_state in data['state'].tolist():
        state_row = data[data['state'] == answer_state]
        guessed_states.append(answer_state)
        print(state_row)
        turtle = t.Turtle()
        t.hideturtle()
        turtle.penup()
        turtle.goto(int(state_row['x']), int(state_row['y']))
        turtle.write(answer_state)
        total_correct +=1
    if answer_state == "Exit":
        # missing_states = []
        # for state in data['state'].tolist():
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #
        missing_states = [state for state in data['state'].tolist() if state not in guessed_states ]
        print(missing_states)
        print(len(missing_states))
        break



screen.exitonclick()