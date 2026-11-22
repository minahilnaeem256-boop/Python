import turtle

screen= turtle.Screen()
screen.bgcolor("black")
screen.title("Colorfull spiral")

pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()

colors=["red","orange","yellow","pink","lime","cyan","violet","white"]

for i in range(120):
    pen.color(colors[i%len(colors)])
    pen.width(2)
    pen.forward(i*2)
    pen.right(90.5)

turtle.done()