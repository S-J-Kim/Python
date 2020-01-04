import datetime

winter = [12,1,2]
spring = [3,4,5] 
summer = [6,7,8] 
fall = [9,10,11]

now = datetime.datetime.now()

if (now.month in winter):
    print("winter")
elif (now.month in spring):
    print("spring")
elif (now.month in summer):
    print("summer")
elif (now.month in fall):
    print("fall")