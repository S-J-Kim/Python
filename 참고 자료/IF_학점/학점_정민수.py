point = input('당신의 학점을 입력해 주세요.:   ')
point = float(point)
if point == 4.5:
    print('당신은 "신"입니다.')
elif 4.2 <= point < 4.5:
    print('당신은 "교수님의 사랑"입니다.')
elif 3.5 <= point < 4.2:
    print('당신은 "현 체제의 수호자"입니다.')
elif 2.8 <= point < 3.5:
    print('당신은 "일반인"입니다.')
elif 2.3 <= point < 2.8:
    print('당신은 "일탈을 꿈꾸는 소시민"입니다.')
elif 1.75 <= point < 2.3:
    print('당신은 "오락문화의 선구자"입니다.')
elif 1.0 <= point < 1.75:
    print('당신은 "불가촉천민"입니다.')
elif 0.5 <= point < 1.0:
    print('당신은 "자벌레"입니다.')
elif 0 < point < 0.5:
    print('당신은 "플랑크톤"입니다.')
elif point == 0:
    print('당신은 "시대를 앞서가는 혁명의 씨앗"입니다.')
else:
    print('잘못 입력하셨습니다. 학점을 0 ~ 4.5 사이를 입력해주세요.')
