n = int(input("정수를 입력하세요"))

if n%2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")


print()
print("끝자리 수로 비교해볼게요")

n = int(input("정수를 입력하세요"))
d = n%10
if d == 0 or d == 2 or d == 4 or d ==6 or d== 8:
    print("짝수입니다")
else:
    print("홀수입니다")
