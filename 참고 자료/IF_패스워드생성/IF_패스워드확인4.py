password = input("정수 4자리 숫자 입력: ")
 
pass1 = int(password[0])    
pass2 = int(password[1])    
pass3 = int(password[2])    
pass4 = int(password[3])    


password2 = (pass1, pass2, pass3, pass4)
if len(password2) != 4 :
        print("4자리 숫자를 입력해주세요: ")

flag = 1

if pass1 in (pass2, pass3, pass4) :
    flag = 0
    print("암호가 중복되어 사용할 수 없습니다")

elif pass2 in (pass3, pass4) :
    flag = 0
    print("암호가 중복되어 사용할 수 없습니다")

elif pass3 == pass4 :
    flag = 0
    print("암호가 중복되어 사용할 수 없습니다")

if pass1+1 == pass2 or pass1+2 == pass3 or pass1+3 == pass4 :
    print("암호가 연속으로 증가되어 사용할 수 없습니다")
    flag = 0

if pass1-1 == pass2 or pass1-2 == pass3 or pass1-3 == pass4 :
    print("암호가 연속으로 증가되어 사용할 수 없습니다")
    flag = 0

if(flag) :
    print("사용할 수 있는 암호입니다")
else :
    print("사용할 수 없는 암호입니다")








