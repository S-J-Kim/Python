age = input('나이 입력 : ')
age = int(age)

if age >= 15: # 입력받은 나이가 15세 이상인 경우
    print("관람 가능")
    print("10000원을 결제합니다")

else: # 입력받은 나이가 15세 미만인 경우
    print("관람 불가")
    print("다른 영화 추천 가능")