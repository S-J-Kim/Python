money1 = int(input("받은돈?"))
money2 = int(input("물건값?"))

change = money1 - money2
change = int(change)
m = change // 10000
print("만원단위는", m,"장")
c = (change - (m*10000)) // 1000
print("천원단위는", c,"장")

