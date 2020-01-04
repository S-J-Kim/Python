
number =int(input("정수를 입력하시오"))
number =str(number)
last_charcater =number[-1]
last_charcater = int(last_charcater)

if last_charcater == 0 or last_charcater == 2 or last_charcater == 4 or last_charcater == 6 or last_charcater ==  8:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")



number = int(input("숫자를 입력하시오: "))


if number % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")