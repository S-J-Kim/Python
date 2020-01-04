import turtle as t

t.shape("turtle")
t.width(3)
t.shapesize(3, 3)

def move_left():
    t.lt(90); t.fd(100) # 왼쪽으로 이동하는 함수

def move_right():
    t.rt(90); t.fd(100) # 오른쪽으로 이동하는 함수

while True:
    command = input("명령어 입력 : ")
    if command == "r": move_right()
    elif command == "l": move_left()
    elif command == "c": t.circle(100)
    else: break # 잘못된 입력을 받으면 종료한다
