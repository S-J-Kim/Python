a = [1, 2, 3, 4, 5]
print(type(a)) # 대괄호는 리스트

b = {1, 2, 3, 4, 5}
print(type(b))  # 중괄호는 딕셔너리

c = (1, 2, 3, 4, 5)
print(type(c)) # 소괄호는 튜플

d = 1, 2, 3, 4, 5
print(type(d))  # 괄호가 없어도 튜플이다

a = []
print(a)  # 리스트의 초기화

c = ()
print(c)  # 튜플의 초기화

a = [1, 2, 3, 4, 5]
a.append(6) # 리스트에 한개의 값 추가
print(a)

a.extend([7, 8, 9]) # 리스트에 여러개의 값 추가
print(a)

a.insert(0, 0)  # 0번 인덱스에 0 추가
print(a)

a.remove(9)  # 리스트의 특정 값 삭제
print(a)

del a[0]
print(a)

a.pop()  # 리스트의 제일 마지막 값 제거
print(a)

a.index(4)  # 특정 값이 있는지 찾기. 있으면 1 없으면 오류
print(a)

a.count(3)  # 특정 값이 몇개 있는지 찾기
print(a)

a.reverse()  # 리스트의 순서를 거꾸로 재정렬
print(a)

a.sort()  # 리스트를 오름차순으로 정렬
print(a)

a.sort(reverse=True)  # 리스트를 내림차순으로 정렬
print(a)
