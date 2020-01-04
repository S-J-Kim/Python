import turtle

t=turtle.Turtle()

t.shape("turtle")

t.pu()

t.goto(110, 100)
t.write("거북이가 여기로 오면 양수입니다")

t.goto(110, 0)
t.write("거북이가 여기로 오면 0입니다")

t.goto(110, -100)
t.write("거북이가 여기로 오면 음수입니다")

t.goto(0, 0)
t.pd()

n = int(input())

if n < 0: t.goto(100, -100)
elif n == 0: t.goto(100, 0)
else: t.goto(100, 100)

turtle.mainloop()