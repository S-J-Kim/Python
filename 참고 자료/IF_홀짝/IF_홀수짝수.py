number = input("정수입력: ")
number = int(number)

number = str(number)

last_number = number[-1]


if last_number == 0 \
   last_number == 2 \
   last_number == 4 \
   last_number == 6 \
   last_number == 8 :
    print("짝수")

else :
    print("홀수")

---------------------------------------------------------

number = input("정수입력: ")
number = int(number)

number = str(number)

last_number = number[-1]

if last_number in '02468' :
    print("짝수")
else :
    print("홀수")


------------------------------------------------------------

number = input("정수입력: ")
number = int(number)

if number % 2 == 0 :
    print("짝수")

else :
    print("홀수")

































