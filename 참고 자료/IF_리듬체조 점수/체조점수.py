a = float(input("A 심사위원의 채점 점수 : "))
b = float(input("B 심사위원의 채점 점수 : "))
c = float(input("C 심사위원의 채점 점수 : "))
d = float(input("D 심사위원의 채점 점수 : "))
e = float(input("E 심사위원의 채점 점수 : "))

ma = max(a,b,c,d,e)
mi = min(a,b,c,d,e)

su = a+b+c+d+e-ma-mi
av = su/3

print("최종 점수는",av,"점 입니다.")
