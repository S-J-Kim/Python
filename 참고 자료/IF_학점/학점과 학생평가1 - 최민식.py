#학생평가

x=float(input("학점을 입력하세요>"))
if x == 4.5 :
    print("학점 {}, 신".format(x))
elif 4.2<= x <=4.5:
    print("학점 {}, 교수님의 사랑".format(x))
elif 3.5<= x <=4.2:
    print("학점 {}, 현 체제의 수호자".format(x))
elif 2.8<= x <=3.5 : 
    print("학점 {}, 일반인".format(x))
elif 2.3<= x <= 2.8:
    print("학점 {}, 일탈을 꿈꾸는 소시민".format(x))
elif 1.75<= x <=2.3:
    print("학점 {}, 오락문화의 선구자".format(x))
elif 1.0<= x <= 1.75:
    print("학점 {}, 불가촉 천민".format(x))
elif 0.5<= x <=1.0:
    print("학점 {}, 자벌레".format(x))
elif 0<= x <=0.5:
    print("학점 {}, 플랑크톤".format(x))
elif x==0.0:
    print("학점 {}, 시대를 앞서가는 혁명의 씨앗".format(x))    
else: 
    print("학점을 소수점 첫째자리까지 정확히 입력하시오.")
