pw = input("패스워드 입력: ")

if len(pw) != 4 :
    print("패스워드를 정수4자리 숫자로 입력해주세요: ")

else :
    if pw.isnumeric() :  # pw가 숫자이면
        a = int(pw[0])
        b = int(pw[1])
        c = int(pw[2])
        d = int(pw[3])

        if (a == b or a == c or a == d) \
           or (b == c or b == d) or (c == d) :
            print("중복된 숫자는 사용할 수 없습니다")

        elif (b == a+1 or c == b+1 or d == c+1) \
           or (b== a-1 or c == b-1 or d == c-1) :
            print("연속으로 증가하거나 감소하는 숫자는 사용할 수 없습니다")
    else :
        print("문자는 입력할 수 없습니다.")
