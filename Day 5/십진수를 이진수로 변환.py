dec = int(input("10진수 입력 : "))

result = ''
while dec > 0:
    remainder = dec % 2
    dec = dec // 2
    result = str(remainder) + result
    
print(f'0b{result}')