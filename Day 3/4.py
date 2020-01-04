# 동전던지기 + 터틀
# 현재 구현 안됨

import random
import turtle

t = turtle.Turtle()

screen = turtle.Screen()

# 이미지파일은 소스랑 같은 경로에 위치해야함
# 경로가 다른 경우엔 경로명까지 입력

img1 = 'f1.PNG'  # 확장자 변경 가능
img2 = 'b1.PNG'
screen.addshape(img1)
screen.addshape(img2)

coin = random.randrange(2)

if coin % 2:
    t.shape(img1)
    t.stamp()

else:
    t.shape(img2)
    t.stamp()

turtle.mainloop()


