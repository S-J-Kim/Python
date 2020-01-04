num = input("점수 입력(스페이스바를 이용한다) : ").split()

runflag = True

if runflag :
    mini = float(min(num))
    print(mini)
    maxi = float(max(num))
    print(maxi)
    a, b, c, d, e = [float(x) for x in num]

    avg = ((a+b+c+d+e)-(mini+maxi))/3
    print(avg)


