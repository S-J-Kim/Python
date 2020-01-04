name = input("이름입력: ")
height = int(input("키 입력: "))
weight = int(input("체중 입력: "))
bmi = weight / (height / 100) ** 2

if bmi > 30 :
    obe = "고도비만"   
if bmi > 25 :
    obe = "비만"
if bmi > 23 :
    obe = "과체중"     
if bmi > 18.5 :
    obe = "정상"
else :
    obe = "저체중"

print("{}님의 키는 {}이고 몸무게는 {}kg 입니다".format(name,height, weight))
print("BMI 지수는 {:.3f}으로 {}입니다".format(bmi, obe))
