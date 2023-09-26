import turtle
import random
turtles = []
turtle.colormode(255)
winner = ""
colors = ["red", "purple", "green", "blue", "black", "orange"]
screen = turtle.Screen()
screen.setup(width=500 , height=400)
user_bet = screen.textinput(title="make a bet", prompt=f'choose the winning color between {colors}:')
for n in range(10):
    tup = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    colors.append(tup)
x = -240
y = 200
for n in range(6):
    tim = turtle.Turtle()
    tim.shape('turtle')
    tim.color(colors[n])
    y = y-50
    tim.penup()
    tim.setposition(x=x, y=y)
    turtles.append(tim)


def exits():
    screen.exitonclick()


if user_bet:
    while True:
        for t in turtles:
            dist = random.randint(0,10)
            t.forward(dist)
            if t.xcor() >= 225:
                winner = t.pencolor()
                if user_bet == winner:
                    print(f"you won! , the winner was {winner}")
                else:
                    print(f"you lost! , the winner was {winner}")

                exits()

