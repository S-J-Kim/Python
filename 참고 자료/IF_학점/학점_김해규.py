score = float(input('학점을 입력하세요 : '))

if score == 4.5:
    print('신')
elif 4.5 > score >= 4.2:
    print('교수님의 사랑')
elif 4.2 > score >= 3.5:
    print('현체재의 수호자')
elif 3.5 > score >= 2.8:
    print('일반인')
elif 2.8 > score >= 2.3:
    print('일탈을 꿈꾸는 소시민')
elif 2.3 > score >= 1.75:
    print('오락문화의 선구자')
elif 1.75 > score >= 1.0:
    print('불가촉 천민')
elif 1.0 > score >= 0.5:
    print('자벌레')
elif 0.5 > score > 0:
    print('플랑크톤')
elif score == 0:
    print('시대를 앞서가는 혁명의 씨앗')
else:
    print('잘못된 입력입니다.')