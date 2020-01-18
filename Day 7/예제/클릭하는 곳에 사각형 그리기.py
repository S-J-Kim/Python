import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def drawit(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()

s = turtle.Screen()
s.onscreenclick(drawit)
turtle.mainloop()