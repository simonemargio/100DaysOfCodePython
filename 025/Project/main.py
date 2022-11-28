import turtle
import pandas


def new_state_text():
    state_text = turtle.Turtle()
    state_text.penup()
    state_text.hideturtle()
    return state_text


def engine():
    correct_state = 0
    while correct_state != 50:
        user_answer = s.textinput(f"{correct_state}/50 States Correct", "What's another state name?").capitalize()
        state = data[data.state == user_answer]

        if user_answer is None:
            exit(0)

        if not state.empty:
            correct_state += 1
            state_text = new_state_text()
            state_text.goto(int(state["x"]), int(state["y"]))
            state_text.write(f"{user_answer}", False, align="center", font=("Courier", 12, "normal"))


data = pandas.read_csv("50_states.csv")

s = turtle.Screen()
s.setup(725, 491)
s.title("U.S States Game")
image = "blank_states_img.gif"
s.addshape(image)

t = turtle.Turtle()
t.shape(image)

engine()

s.mainloop()
