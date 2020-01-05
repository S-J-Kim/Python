import turtle
import random

t = turtle.Turtle("turtle")

for i in range(30):
    length = random.randint(1, 100)
    angle = random.randint(-180, 180)
    
    if length % 2: t.fd(length)
    else: t.bk(length)

    if angle % 2: t.lt(angle)
    else: t.rt(angle)

turtle.mainloop()