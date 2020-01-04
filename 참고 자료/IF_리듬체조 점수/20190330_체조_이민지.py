num = input("점수 입력(스페이스바를 이용한다) : ").split()
num = list(num)
runflag = True

if runflag :
    mini = float(min(num))
    maxi = float(max(num))
    a, b, c, d, e = [float(x) for x in num]

    avg = ((a+b+c+d+e)-(mini+maxi))/3
    print(avg)


