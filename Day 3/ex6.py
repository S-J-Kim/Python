months_after_birth = input("아이가 태어난지 몇 개월입니까? : ")
months_after_birth = int(months_after_birth)

if months_after_birth < 0: print("다시 입력하세요") # 0미만의 숫자는 입력받을 수 없음

if months_after_birth < 1:
    print('결핵 예방접종 대상자입니다.')
if months_after_birth <= 1:
    print('B형간염 예방접종 대상자입니다.')
if 2 <= months_after_birth <= 6:
    print('파상풍 예방접종 대상자입니다.')
if 2 <= months_after_birth <= 15:
    print('폐렴구균 예방접종 대상자입니다.')

else: print('예방접종 대상자가 아닙니다.') # 태어난지 15개월을 초과했다면 맞을 수 있는 예방접종이 없음