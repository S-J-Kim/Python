# 사용자로부터 4자리 수의 암호를 입력받아 검증하는 프로그램
# 사용가능한 암호가 입력될 때까지 반복해서 입력받는다.

# 사용가능한 암호의 조건
# 조건1: 중복되는 숫자가 없어야한다.	ex) 1231, 5151, 7807
# 조건2: 4연속 1씩 증가되면 안된다.	ex) 1234, 6789
# 조건3: 4연속 1씩 감소되면 안된다.	ex) 9876, 3210

def verify():
	password = input("사용할 네 자리수 암호입력: ")
	p1 = int(password[0])
	p2 = int(password[1])
	p3 = int(password[2])
	p4 = int(password[3])

	duplicate = p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4
	increment = p1 + 1 == p2 or p2 + 1 == p3 or p3 + 1 == p4
	decrement = p1 - 1 == p2 or p2 - 1 == p3 or p3 - 1 == p4
	bad_password = duplicate or increment or decrement

	if bad_password:
		return False
	else:
		return True

