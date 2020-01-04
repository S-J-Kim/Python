i = float(input("학점 : "))

num = [0, 0.5 ,1.0, 1.75, 2.3, 2.8, 3.5, 4.2, 4.5]
desc = ["신","교수님의 사랑", "현 체제의 수호자", "일반인", \
        "일탈을 꿈꾸는 소시민", "오락문화의 선구자", "불가촉천민", "자벌레", \
        "플랑크톤", "시대를 앞서가는 혁명의 씨앗"]
desc.reverse()
index = 0

for a in range(0, 9) :
    if i == 0 :
        index = 0
    elif num[a] < i < num[a+1] :
        print("{} < {} < {}".format(num[a], i , num[a+1]))
        index = a+1
    elif i== 4.5 :
        index=9

print("당신은 {}입니다.".format(desc[index]))
