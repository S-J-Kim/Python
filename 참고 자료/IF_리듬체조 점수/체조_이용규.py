a = float(input("첫번째 심사위원 점수 : "))
b = float(input("두번째 심사위원 점수 : "))
c = float(input("세번째 심사위원 점수 : "))
d = float(input("네번째 심사위원 점수 : "))
e = float(input("다섯번째 심사위원 점수 : "))

array = [a,b,c,d,e]
maxNum = max(array)
minNum = min(array)

print("최고점  : " , maxNum)
print("최저점  : " , minNum)

sumCount = sum(array) - maxNum - minNum

print(sumCount)
print(len(array) -2)
average = sumCount / (len(array) -2)

print("총합 : " , sumCount)
print("평균 : " , average)

