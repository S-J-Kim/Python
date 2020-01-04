# 1

print("수를 입력하세요:")
a=int(input())

if a % 2 == 0 :
    print("{}은(는) 짝수입니다.".format(a))
else :
    print("{}은(는) 홀수입니다.".format(a))


# 2

print('수를 입력하세요.')
a = input()

b = int(a[-1:])

if b == 2 or b == 4 or b == 6 or b == 8 or b == 10:
    print("{}은(는) 짝수입니다.".format(a))
else :
    print("{}은(는) 홀수입니다.".format(a))


# 3

print("수를 입력하세요:")
a=input()

b=[2,4,6,8,0]

c=int(a[-1:])

if c in b:
    print("{}은(는) 짝수입니다.".format(a))
else :
    print("{}은(는) 홀수입니다.".format(a))