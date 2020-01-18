import turtle
t = turtle.Turtle()

def drawit(x, y):
    t.goto(x, y)
    
s = turtle.Screen()
s.onscreenclick(drawit)
turtle.mainloop()