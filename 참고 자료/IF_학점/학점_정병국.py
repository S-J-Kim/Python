a = float(input("학점을 입력하세요:\n"))

if a == 4.5:
    print("{}점은 신 입니다.".format(a))

if 4.2 <= a < 4.5:
    print("{}점은 교수님의 사랑 입니다.".format(a))

if 3.5 <= a < 4.2:
    print("{}점은 현 체제의 수호자 입니다.".format(a))

if 2.8 <= a < 3.5:
    print("{}점은 일반인 입니다.".format(a))

if 2.3 <= a < 2.8:
    print("{}점은 일탈을 꿈꾸는 소시민 입니다.".format(a))

if 1.75 <= a < 2.3:
    print("{}점은 오락문화의 선구자 입니다.".format(a))

if 1.0 <= a < 1.75:
    print("{}점은 불가촉천민 입니다.".format(a))

if 0.5 <= a < 1.0:
    print("{}점은 자벌레 입니다.".format(a))

if 0 < a < 0.5:
    print("{}점은 플랑크톤 입니다.".format(a))
    
if a == 0:
    print("{}점은 시대를 앞서가는 혁명의 씨앗 입니다.".format(a))