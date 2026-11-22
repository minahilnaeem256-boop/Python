import turtle

screen= turtle.Screen()
screen.bgcolor("black")
screen.title("colorful petals")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

petal_colors=["pink","cyan","purple","orange","yellow","violet"]
for i in range(36):

    board.color(petal_colors[i% len(petal_colors)],
                petal_colors[(i+2)% len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

turtle.done()