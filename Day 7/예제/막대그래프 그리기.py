import turtle

t = turtle.Turtle()

def drawbar(height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(str(height), font=("Times New Roman", 16, "bold"))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

data = [129, 56, 369, 229, 158, 23, 89]

t.color("Dark Salmon")
t.fillcolor("coral")
t.pensize(3)

for d in data:
    drawbar(d)

turtle.mainloop()