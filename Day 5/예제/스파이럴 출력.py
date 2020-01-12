import turtle as t


colors=['Dark Salmon', 'Salmon', "Light Salmon", 'Orange', 'Dark Orange', "Coral", 'Light Coral', "Tomato", "Orange Red"]
#t = turtle.Turtle()
t.bgcolor("Dark Slate Gray")
t.speed(0)
t.width(3)

length = 30

while length < 1000:
    t.fd(length)
    t.pencolor(colors[length % (len(colors))])
    t.rt(89)
    length += 5
    
t.mainloop()
