import turtle

t = turtle.Turtle()
t.shape("classic")  # 커서 모양 지정

size = int(input("사이즈를 입력하세요 : "))

t.fd(size); t.rt(90)
t.fd(size); t.rt(90)
t.fd(size); t.rt(90)
t.fd(size); t.rt(30)  # 사각형 그리기를 마치고 삼각형을 그림
t.fd(size); t.rt(120)
t.fd(size)

