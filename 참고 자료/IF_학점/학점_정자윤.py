# 학점, 학생평가 
print("학점을 입력하세요")
n=float(input())
if n==4.5:
    print('{}학점, 신'.format(n))
if 4.2<=n<4.5:
    print('{}학점, 교수님의 사랑'.format(n))
if 3.5<=n<4.2:
    print('{}학점, 현 제체의 수호자'.format(n))
if 2.8<=n<3.5:
    print("{}학점, 일반인".format(n))
if 2.3<=n<2.8:
    print("{}학점, 일탈을 꿈꾸는 소시민".format(n))
if 1.75<=n<2.3:
    print("{}학점, 오락문화의 선구자".format(n))
if 1.0<=n<1.75:
    print("{}학점, 불가촉천민".format(n))
if 0.5<=n<1.0:
    print("{}학점, 자벌레".format(n))
if 0<n<0.5:
    print("{}학점, 플랑크톤".format(n))
if n==0:
    print("{}학점, 시대를 앞서가는 혁명의 씨앗".format(n))
input('확인이 끝나셨으면 엔터를 쳐주세요.')
