num = input() # 정수를 입력받는다.
num = int(num)

thousand = (num % 10) * 1000 # 일의 자리를 천의 자리로 바꿈
hundred = ((num // 10) % 10) * 100
ten = ((num // 100) % 10) * 10
one = num // 1000

res = thousand + hundred + ten + one # 결과를 다 더한다

print(res)

    
