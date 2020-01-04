
def calc() :
    return ((change-(change % unit[i]))/unit[i])


unit = [50000, 10000, 5000, 1000, 100, 50, 10]
unitCount = 0

input_money = int(input("투입한 금액 > "))
price = int(input("물건 값 > "))

change = input_money - price
print ('거스름돈 > ' + str(change))

for i in range(0,len(unit),1) : 
    unitCount = calc()
    print(str(unit[i])+"짜리 동전 : "+str(unitCount))
    change = change - unit[i]*unitCount
    
