import turtle 
turtle.Screen()
turtle.bgcolor("black")
turtle.title("petals")

pen=turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()
pen.pensize(2)

def draw(size,colour):
    pen.color(colour)
    pen.begin_fill()

    for i in range(2):
        pen.circle(size,60)
        pen.left(120)
    pen.end_fill()

colours=["pink","yellow","red","cyan","orange","lime","blue","magenta"]
for i in range(36):
    draw(90,colours[i%len(colours)])
    pen.right(10)

pen.penup()
pen.goto(0,-15)
pen.pendown()

pen.color("beige")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

turtle.done()



