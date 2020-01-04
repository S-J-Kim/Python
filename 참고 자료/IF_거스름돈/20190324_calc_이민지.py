print("########################")
#입력 값
input_money = int(input("투입한 돈 : "))
product_value = int(input("물건 값 : "))

#거스름돈 계산 
change = input_money - product_value
print("########################")
print()
print("거스름돈 : " + str(change))
print()

#거스름돈 출력 
if change > 1000 :
    paper = change // 1000
    coins = change % 1000

    print("\t1000원 지폐 : " + str(paper))
      
    if coins > 500 :
        coin500s = coins // 500
        coin100s = (coins % 500) //100
        print("\t500원 동전 : "  + str(coin500s))
        print("\t100원 동전 : "+ str(coin100s))
        
    else :
        coin100s = coins // 100
        print("\t100원 동전 : " + str(coin100s))


print("########################")
