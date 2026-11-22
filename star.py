import turtle

screen= turtle.Screen()
screen.bgcolor("black")
screen.title("goldenStar")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

board.penup()
board.setheading(90)
board.pendown()

board.color("gold","yellow")
board.width(4)
board.begin_fill()

for i in range(5):
    board.forward(130)
    board.right(144)

board.end_fill()
turtle.done()