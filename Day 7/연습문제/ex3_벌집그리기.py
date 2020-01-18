import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("turtle")

def hexagon():
    for i in range(6):
        t.fd(100)
        t.lt(60)
        for j in range(6):
            t.fd(100)
            t.rt(60)

hexagon()
turtle.mainloop()
