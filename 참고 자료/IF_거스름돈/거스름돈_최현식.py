a = input("구매금액은 얼마인가요 >> ")
b = input("입금금액은 얼마인가요 >> ")
if int(a) > int(b):
    print("입금금액보다 구매금액이 클 수 없습니다.")
c = int(b) - int(a)
if int(c) > 0:
    cash50000 = int(c/50000)
    c = c - (cash50000 * 50000)
if int(c) > 0:    
    cash10000 = int(c/10000)
    c = c - (cash10000 * 10000)
if int(c) > 0:
    cash5000 = int(c/5000)
    c = c - (cash5000 * 5000)
if int(c) > 0:
    cash1000 = int(c/1000)
    c = c - (cash1000 * 1000)
print("=======================")
print("구매금액:{}원".format(a))
print("입금금액:{}원".format(b))
print("5만원권:{}장".format(cash50000))
print("1만원권:{}장".format(cash10000))
print("5천원권:{}장".format(cash5000))
print("1천원권:{}장".format(cash1000))
print("잔액:{}원".format(c))
print("=======================")