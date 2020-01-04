import turtle
t = turtle.Turtle()
t.shape('turtle')  # 3번라인 생략시 기본커서사용

# 사용자에게 집의 크기 질문
size = int(input("크기를 입력하세요: "))

# 사각형 그리기
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

# 지붕그리기
t.right(90)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)



