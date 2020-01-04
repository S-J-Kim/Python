pw = input("4자리 숫자로된 암호를 입력해주세요: ")

if pw[0] == pw[1] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")
elif pw[0] == pw[2] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")
elif pw[0] == pw[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")

elif pw[1] == pw[2] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")
elif pw[1] == pw[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")

elif pw[2] == pw[3] :
    print("암호에 중복된 숫자는 사용할 수 없습니다")

elif int(pw[0])+1 == int(pw[1]) :
    print("암호에 연속으로 증가하는 숫자는 사용할 수 없습니다")
elif int(pw[1])+1 == int(pw[2]) :
    print("암호에 연속으로 증가하는 숫자는 사용할 수 없습니다")
elif int(pw[2])+1 == int(pw[3]) :
    print("암호에 연속으로 증가하는 숫자는 사용할 수 없습니다")

elif int(pw[0])-1 == int(pw[1]) :
    print("암호에 연속으로 감소되는 숫자는 사용할 수 없습니다")
elif int(pw[1])-1 == int(pw[2]) :
    print("암호에 연속으로 감소되는 숫자는 사용할 수 없습니다")
elif int(pw[2])-1 == int(pw[3]) :
    print("암호에 연속으로 감소되는 숫자는 사용할 수 없습니다")

else :
    print("사용할 수 있는 암호입니다")

print()
input("Press Enter to clse....")







