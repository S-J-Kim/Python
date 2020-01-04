num = float(input("학점을 입력하세요."))

if num == 4.5:
    print("당신의 학점은 {}이며, 설명은 '신' 입니다.".format(num))
elif 4.2 <= num <= 4.49:
    print("당신의 학점은 {}이며, 설명은 교수님의 사랑 입니다.".format(num))
elif 3.5 <= num <= 4.19:
    print("당신의 학점은 {}이며, 설명은 현 체제의 수호자 입니다.".format(num))
elif 2.8 <= num <= 3.49:
    print("당신의 학점은 {}이며, 설명은 일반인 입니다.".format(num))
elif 2.3 <= num <= 2.79:
    print("당신의 학점은 {}이며, 설명은 일탈을 꿈꾸는 소시민 입니다.".format(num))
elif 1.75 <= num <= 2.29:
    print("당신의 학점은 {}이며, 설명은 오락문화의 선구자 입니다.".format(num))
elif 1.0 <= num <= 1.74:
    print("당신의 학점은 {}이며, 설명은 불가촉천민 입니다.".format(num))
elif 0.5 <= num <= 0.99:
    print("당신의 학점은 {}이며, 설명은 자벌레 입니다.".format(num))
elif 0 <= num <= 0.49:
    print("당신의 학점은 {}이며, 설명은 플랑크톤 입니다.".format(num))
else:
    print("당신의 학점은 {}이며, 설명은 시대를 잘못 타고난 사람 입니다.".format(num))