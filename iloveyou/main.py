import turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title("I love you")

    pen = turtle.Turtle()
    pen.speed(1)
    pen.color("red")
    pen.hideturtle()

    pen.penup()
    pen.goto(-120, 0)
    pen.pendown()
    pen.write("I", align="center", font=("Arial", 60, "normal"))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("red")
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

    pen.penup()
    pen.goto(120, 0)
    pen.pendown()
    pen.write("you", align="center", font=("Arial", 60, "normal"))

    pen.hideturtle()
    turtle.done()