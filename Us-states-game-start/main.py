import turtle

import pandas

screen = turtle.Screen()
tur = turtle.Turtle()

screen.title("U.S States Game")

image = "./blank_states_img.gif"
screen.addshape(image)  # Add the image as a shape
tur.shape(image)  # Create a turtle and set its shape to the image

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missed_states = []

# # Find x,y coordinates, mouse click
# def on_click_get_coordinates(x, y):
#     print(f"Clicked at {x}, {y}")
#
#
# screen.onscreenclick(on_click_get_coordinates)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="what's another stats name ? ").title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("./missed_states.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # Fetch particular row for the guessed state
        t.goto(state_data.x.item(), state_data.y.item())  # Extract scalar values. using .item()
        t.write(state_data.state.item())  # Extract scalar values. using .item()
    else:
        print("wrong entry")


