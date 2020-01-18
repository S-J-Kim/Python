import turtle
import random

t = turtle.Turtle()

def draw_maze(x, y):
    for i in range(2):
        t.pu()
        if i == 1:
            t.goto(x + 100, y + 100)
            
        else:
            t.goto(x, y)
        t.pd()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)

# 거북이를 왼쪽으로 회전하여 10만큼 전진
def turn_left():
    t.lt(10)
    t.fd(10)

# 거북이를 오른쪽으로 회전하여 10만큼 전진    
def turn_right():
    t.rt(10)
    t.fd(10)

t.speed(0)
s = turtle.Screen()

draw_maze(-300, 200)
s.onkey(turn_left, "Left")  # 왼쪽 방향키 입력
s.onkey(turn_right, "Right")  # 오른쪽 방향키 입력

t.pu()
t.goto(-300, 200)
t.speed(1)
t.pd()
s.listen()
s.mainloop()





