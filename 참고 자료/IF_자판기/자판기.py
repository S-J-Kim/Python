print("사이다-700원  콜라-800원  물-1200원")

money = input("돈을 넣어주세요: ")
money = int(money)

drink = int(input("선택) 1-사이다  2-콜라  3-물"))

if drink == 1 and money >= 700 :
    print("사이다가 나왔습니다. 덜컹")
    money = money - 700
elif drink == 2 and money >= 800 :
    print("콜라가 나왔습니다. 덜컹")
    money = money - 800
elif drink == 3 and money >= 1200 :
    print("물이 나왔습니다. 덜컹")
    money = money - 1200
else :
    print("금액이 부족하여 선택할 수 없습니다")

if money >= 0 :
    print("거스름돈 {}원 반환합니다.".format(money))
    
