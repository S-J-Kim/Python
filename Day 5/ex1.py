import turtle

t = turtle.Turtle()
#t.color("blue")
t.shape("turtle")

colorset = ["red", "green", "blue"]

i = 12

t.lt(90)

while i > 0:
    t.color(colorset[(i % 3) - 1])
    t.penup()
    t.fd(30)
    t.pd()
    t.fd(30)
    t.pu()
    t.fd(30)
    t.stamp()
    t.bk(90)
    # t.home() 원래자리로 되돌아감.
    t.rt(30)
    i -= 1
    
turtle.mainloop()