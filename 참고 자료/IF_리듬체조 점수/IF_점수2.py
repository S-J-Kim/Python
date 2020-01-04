num = input("점수 입력 : ").split()

runflag = True

if runflag :
    mini = min(num)
    maxi = max(num)
    a, b, c, d, e = [float(x) for x in num]

    avg = (((a+b+c+d+e) - (float(mini)+float(maxi))) / 3)
    print(avg)


