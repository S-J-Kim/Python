# lambda expression
print((lambda x: x + 10)(1))

# 람다 표현식을 인수로 사용할 수 있음
def plus_ten(x):
    return x + 10

print(list(map(plus_ten, [1, 2, 3])))
print(list(map(lambda x: x + 10, [3, 4, 5])))
