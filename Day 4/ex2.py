password = input()

def isOverlap(s): # 네 개의 숫자 중 중복이 있는지 확인한다.
    state = False

    if s[0] == s[1] or s[0] == s[2] or s[0] == s[3]: state = True
    if s[1] == s[2] or s[1] == s[3]: state = True
    if s[2] == s[3]: state = True
    
    return state
 
def isAscending(s): # 네 개의 숫자가 오름차순으로 배치되어 있는지 확인한다.
    if ((int(s[0]) + 3) % 10) == ((int(s[1]) + 2) % 10) == ((int(s[2]) + 1) % 10) == ((int(s[3]) % 10)): return True
    else: return False

def isDescending(s): # 네 개의 숫자가 내림차순으로 배치되어 있는지 확인한다.
    if ((int(s[3]) + 3) % 10) == ((int(s[2]) + 2) % 10) == ((int(s[1]) + 1) % 10) == ((int(s[0]) % 10)): return True
    else: return False

if isOverlap(password) or isAscending(password) or isDescending(password): print("사용할 수 없는 암호입니다") # 조건에 하나라도 맞지 않으면 그 비밀번호는 사용할 수 없음
else: print("사용할 수 있는 암호입니다.")    

