money = int(input("받은 돈: "))
price = int(input("물건 값: "))

change = money - price
print("거스름돈: ", change)


fifty_thousand = int(change / 50000)
change = change % 50000

ten_thousand = int(change / 10000)
change = change % 10000

five_thousand = int(change / 5000)
change = change % 5000

one_thousand = int(change / 1000)

print() #공백
print() #공백
print("거스름돈은 다음과 같습니다")
print() #공백
print("50000원짜리 지폐 : " + str(fifty_thousand) + "장")
print("10000원짜리 지폐 : " + str(ten_thousand) + "장")
print("5000원짜리 지폐 : " + str(five_thousand) + "장")
print("1000원짜리 지폐 : " + str(one_thousand)+ "장")
