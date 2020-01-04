# 1 [기본]

score = input ("학점 : ")
score = float (score)

if score == 4.5:
    print ("{}: 신".format(score))
elif score >= 4.2:
    print ("{}: 교수님의 사랑".format(score))
elif score >= 3.5:
    print ("{}: 현 체제의 수호자".format(score))
elif score >= 2.8:
    print ("{}: 일반인".format(score))
elif score >= 2.3:
    print ("{}: 일탈을 꿈꾸는 소시민".format(score))
elif score >= 1.75:
    print ("{}: 오락문화의 선구자".format(score))
elif score >= 1.0:
    print ("{}: 불가촉천민".format(score))
elif score >= 0.5:
    print ("{}: 자벌레".format(score))
elif score > 0:
    print ("{}: 플랑크톤".format(score))
else:
    print ("{}: 시대를 앞서가는 혁명의 씨앗".format(score))


# 2 [리스트 만든 후 변화]

score = input ("학점 : ")
score = float (score)

a = [4.5, 4.2, 3.5, 2.8, 2.3, 1.75, 1.0, 0.5, 0]

if score == a[0]:
    print ("{}: 신".format(score))
elif score >= a[1]:
    print ("{}: 교수님의 사랑".format(score))
elif score >= a[2]:
    print ("{}: 현 체제의 수호자".format(score))
elif score >= a[3]:
    print ("{}: 일반인".format(score))
elif score >= a[4]:
    print ("{}: 일탈을 꿈꾸는 소시민".format(score))
elif score >= a[5]:
    print ("{}: 오락문화의 선구자".format(score))
elif score >= a[6]:
    print ("{}: 불가촉천민".format(score))
elif score >= a[7]:
    print ("{}: 자벌레".format(score))
elif score > a[8]:
    print ("{}: 플랑크톤".format(score))
else:
    print ("{}: 시대를 앞서가는 혁명의 씨앗".format(score))
