# 숙제 1 : 최대공약수 구하기 (유클리드 호제법 사용)
def FindGcd(num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)
    
    if big % small == 0: return small # big이 small로 나누어 떨어지면, big과 small의 최대공약수는 small이다.
    else: return FindGcd(small, big % small)

a, b = input().split()
print(FindGcd(int(a), int(b)))
