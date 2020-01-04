
n = float(input("학점을 입력하세요 : "))


if n == 4.5:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "신"))
elif 4.2 <= n < 4.5:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "교수님의 사랑"))
elif 3.5 <= n < 4.2:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "현 체제의 수호자"))
elif 2.8 <= n < 3.5:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "일반인"))
elif 2.3 <= n < 2.8:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "일탈을 꿈꾸는 소시"))
elif 1.75 <= n < 2.3:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "오락문화의 선구"))
elif 1. <= n < 1.75:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "불가촉천민"))
elif 0.5 <= n < 1.0:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "자벌레"))
elif 0 < n < 0.5:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "플랑크톤"))
elif n == 0:
    print("학점 {}을 받으신 당신은 {}입니다".format(n, "시대를 앞서가는 혁명의 씨앗"))
else:
    print("그럴리가 없어요:(")
