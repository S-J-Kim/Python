num1 = int(input("첫번째 큰수를 입력: "))
num2 = int(input("두번째 작은수를 입력: "))

Add = num1 + num2
Sub = num1 - num2
PRo = num1 * num2
Div = num1 / num2

print("{} + {} = {}".format(num1, num2, Add))

print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))


print("두수의 합은{0}, 두수의 차는{1}, 두수의 곱은{2}, 두수의나눈값은{3}".\
format(num1+num2, num1-num2, num1*num2, num1/num2))

