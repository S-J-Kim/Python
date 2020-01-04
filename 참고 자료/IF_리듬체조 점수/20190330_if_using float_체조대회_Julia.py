#다섯명 심판의 점수를 입력받기
s1 = float(input("점수 1 :"))
s2 = float(input("점수 2 :"))
s3 = float(input("점수 3 :"))
s4 = float(input("점수 4 :"))
s5 = float(input("점수 5 :"))


sum_s=s1+s2+s3+s4+s5
print("합은 ",sum_s)
max1=s1
min1=s1

if s2>max1 :
    max1 = s2
elif s2<min1 :
    min1 = s2
elif s3>max1 :
    max1 = s3
elif s3<min1 :
    min1 = s3
elif s4>max1 :
    max1 = s4
elif s4<min1 :
    min1 = s4
elif s5> max1 :
    max1 = s5
elif s5<min1 :
    min1 = s5
print("max값은 ",max1)
print("min값은 ", min1)



aver_s=(sum_s-max1-min1)/3

print("평균은 ", aver_s)
