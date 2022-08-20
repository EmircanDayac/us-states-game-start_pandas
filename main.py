import turtle
from turtle import Screen
import pandas

_pandas_csv = pandas.read_csv("50_states.csv")
data2 = _pandas_csv.state.to_list()
print(_pandas_csv)
print(data2)

Detect = 0
_screen = Screen()
_screen.title("Game U.S.A DETECT")
image = "blank_states_img.gif"
_screen.addshape(image)
turtle.shape(image)
Correct = []

while len(Correct) < 50:
    _input2 = _screen.textinput(f"Score = {len(Correct)}/50", "Get City Name")
    for _input in data2:
        Correct.append(_input2)
        t = turtle.Turtle()
        t.penup()
        t.color("black")
        t.hideturtle()
        state_data = _pandas_csv[_pandas_csv.state == _input2]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(_input2)
        _input2 = _screen.textinput(f"Score = {len(Correct)}/50", "Get City Name")
