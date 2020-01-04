x = (input('학점 << '))
if x == "":
    x = -1
x = float(x)
res = ""
if 4.5 <= x:
    res = "신"
elif 4.2 <= x and x < 4.5:
    res = "교수님의 사랑"
elif 3.5 <= x and x < 4.2:
    res = "현 체제의 수호자"
elif 2.8 <= x and x < 3.5:
    res = "일반인"
elif 2.3 <= x and x < 2.8:
    res = "일탈을 꿈꾸는 소시민"
elif 1.75 <= x and x < 2.3:
    res = "오락문화의 선구자"
elif 1.0 <= x and x < 1.75:
    res = "불가촉천민"
elif 0.5 <= x and x < 1.0:
    res = "자벌레"
elif 0 <= x and x < 0.5:
    res = "플랑크톤"
elif x < 0:
    x = "오류"
    res = "잘못입력하셨습니다"
print("학점:{}, 등급:{}".format(str(x),res))