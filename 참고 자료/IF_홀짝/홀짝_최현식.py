# 홀짝표시
# 입력받음
# 0포함
# 정수에 한함
# 출력('x은 (홀,짝)수입니다')
# 1
x = input('임의의 정수를 입력해주세요 >> ')
res = ""
if (int(x)%2 == 0):
    res = "짝" 
else:
    res = "홀"
print("{}은 {}수입니다.".format(x,res))
# 2
list_num = [0,2,4,6,8]
x = input('임의의 정수를 입력해주세요 >> ')
res = ""
if int(x[-1]) in list_num:
    res = "짝" 
else:
    res = "홀"
print("{}은 {}수입니다.".format(x,res))
