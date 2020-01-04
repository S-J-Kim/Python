# 입력받은 숫자가 짝수인지 표현

L = [0,2,4,6,8]
num=int(input("숫자를 입력하세요 : "))
if num%10 in L:
            print("입력한 숫자는 {} 짝수입니다".format(num))
else:   
            print("입력한 숫자는 {} 홀수입니다".format(num))

input("Press Enter to close")

   
