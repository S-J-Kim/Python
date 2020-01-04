#다섯심판의 점수를 받아서 최고와 최저를 배제하고 나머지 3개로 평균점숫를 구한다

j1 = float(input("점수1을 입력하세요  : "))
j2 = float(input("점수2을 입력하세요  : "))
j3 = float(input("점수3을 입력하세요  : "))
j4 = float(input("점수4을 입력하세요  : "))
j5 = float(input("점수5을 입력하세요  : "))

#최대값과 최소값을 구한다
max = min = j1
if j2>max:
    max=j2
elif j2<min:
    min = j2

if j3>max:
    max=j3
elif j3<min:
    min = j3

if j4>max:
    max=j4
elif j4<min:
    min = j4
        
if j5>max:
    max=j5
elif j5<min:
    min = j5  

average=((j1+j2+j3+j4+j5)-(max+min))/3

print()
print("최종점수는 {:.3f} 입니다".format(average))

     
           
