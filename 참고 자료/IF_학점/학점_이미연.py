score = float(input("학점을 입력하시오: "))

if score == 4.5:
    print("신")
if 4.2 <= score <4.5:
    print("교수님의 사랑")
if 3.5 <= score <4.2:
    print("현 체제의 수호자")
if 2.8 <= score <3.5:
    print("일반인")
if 2.3 <= score <2.8:
    print("일탈을 꿈꾸는 소시민")
if 1.75 <= score <2.3:
    print("오락문화의 선구자")
if 1.0 <= score <1.75:
    print("불가촉천민")
if 0.5 <= score <1.0:
    print("자벌레")
if 0 < score <0.5:
    print("플랑크톤")
if 0 == score :
    print("시대를 앞서가는 혁명의 씨앗")
else:
    print("초신성")