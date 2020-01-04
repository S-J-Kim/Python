expList = ['신', '교수님 사랑','현 체제의 수호자', '일반인', '일탈을 꿈꾸는 소시민', '오락문화의 선구자', '불가촉천민', '자벌레', '플랑크톤', '시대를 앞서가는 혁명의 씨앗']
score = float(input("학점을 입력하세요(0 ~ 4.5)(종료 -1) : "))
while score != -1 :
    
    if score == 4.5 :
        print(">> "+expList[0])
    elif 4.2 <= score < 4.5 :
        print(">> "+expList[1])
    elif 3.5 <= score < 4.2 :
        print(">> "+expList[2])
    elif 2.8 <= score < 3.5 :
        print(">> "+expList[3])
    elif 2.3 <= score < 2.8 :
        print(">> "+expList[4])
    elif 1.75 <= score < 2.3 :
        print(">> "+expList[5])
    elif 1.0 <= score < 1.75 :
        print(">> "+expList[6])
    elif 0.5 <= score < 1.0 :
        print(">> "+expList[7])
    elif 0 < score < 0.5 :
        print(">> "+expList[8])
    elif score == 0 :
        print(">> "+expList[9])
    else :
        print(">> 학점의 범위는 0 ~ 4.5 입니다. 다시 입력해주세요.")

    score = float(input("학점을 입력하세요(0 ~ 4.5)(종료 -1) : "))