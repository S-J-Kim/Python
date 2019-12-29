c = '''어서와
파이썬은
처음이지?''' # 여러줄을 포함하는 문자열

print(c)

a = "Hello" 
print(a.find("ll"))  # 찾는 문자열이 위치하는 인덱스 반환

s = '    strip  '
print(s.strip())  # 문자열 좌우의 공백을 제거

src = "Hello, World"
dest = src.replace("World", "Python")  # 특정 문자열을 원하는 문자열로 변경
print(dest)

k = 'Apple, Orange, Kiwi'
l = k.split(', ') # 구분자를 통해 문자열을 리스트로 분리
print(l)

print("{0:>10}".format("apple")) # 오른쪽 정렬
print("{0:^10}".format("apple")) # 가운데 정렬
print("{0:<10}".format("apple")) # 왼쪽 정렬

print("{0:@^15}".format('apple')) # 가운데 정렬 후 공백 채우기
print("{0:*<15}".format('apple'))  # 왼쪽 정렬 후 공백 채우기

name = "홍길동"
number = "010-3311-1133"
e_mail = "example@email.com"
print(f'나의 이름은 {name}이고, 번호는 {number}입니다. 이메일 주소는 {e_mail}입니다.')  # 조금 더 편리한 방법으로 출력하기

print(f'{"hi":<10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬
print(f'{"hi":>10}')  # 왼쪽 정렬

print(f'{"hi":%<10}')
print(f'{"hi":%^10}')
print(f'{"hi":%>10}')

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

print(f'{a} * {b} = {a*b}')