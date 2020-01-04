#학점을 입력하면 학생평가출력

num=input("학점을 입력하세요: ")


if float(num)==0:
    print("학점{} 는 '시대를 앞서가는 혁명의 씨앗'".format(float(num)))
elif   0<float(num)<0.5:
    print("학점{} 는  '플랑크톤'".format(float(num)))
elif   0.5<=float(num)<1.0:
    print("학점{} 는  '자벌레'".format(float(num)))
elif   1.0<=float(num)<1.75:
    print("학점{} 는 '불가촉천민'".format(float(num)))
elif   1.75<=float(num)<2.3:
    print("학점{} 는  '오락문화의 선국자'".format(float(num)))
elif   2.3<=float(num)<2.8:
    print("학점{} 는  '일탈을 꿈꾸는 소시민'".format(float(num)))
elif   2.8<=float(num)<3.5:
    print("학점{} 는  '일반인'".format(float(num)))
elif   3.5<=float(num)<4.2:
    print("학점{} 는  현 체제의 수호자".format(float(num)))
elif   4.2<=float(num)<4.5:
    print("학점{} 는  '교수님의 사랑'".format(float(num)))
elif   float(num)==4.5:
    print("학점{} 는  '신'".format(float(num)))

print()
input("Press enter to close...")
          
