l = [1, 2, 3, 4, 5]
print(type(l)) # 대괄호는 리스트

b = {1, 2, 3, 4, 5}
print(type(b))  # 중괄호는 딕셔너리

c = (1, 2, 3, 4, 5)
print(type(c)) # 소괄호는 튜플

d = 1, 2, 3, 4, 5
print(type(d))  # 괄호가 없어도 튜플이다

l = []
print(l)  # 리스트의 초기화

c = ()
print(c)  # 튜플의 초기화

l = [1, 2, 3, 4, 5]
l.append(6) # 리스트에 한개의 값 추가
print(l)

l.extend([7, 8, 9]) # 리스트에 여러개의 값 추가
print(l)

l.insert(0, 0)  # 0번 인덱스에 0 추가
print(l)

l.remove(9)  # 리스트의 특정 값 삭제
print(l)

del l[0]
print(l)

l.pop()  # 리스트의 제일 마지막 값 제거
print(l)

l.index(4)  # 특정 값이 있는지 찾기. 있으면 1 없으면 오류
print(l)

l.count(3)  # 특정 값이 몇개 있는지 찾기
print(l)

l.reverse()  # 리스트의 순서를 거꾸로 재정렬
print(l)

l.sort()  # 리스트를 오름차순으로 정렬
print(l)

l.sort(reverse=True)  # 리스트를 내림차순으로 정렬
print(l)
