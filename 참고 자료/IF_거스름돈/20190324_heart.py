import turtle as t

t.speed(1)
t.color('black', 'red')
t.begin_fill()
#create ♥
t.lt(50)
t.fd(123)

for i in range(0, 2) :
    for j in range (0, 230) :
        t.lt(1)
        t.fd(1)
        
    if i == 0 :
        t.rt(180)
    if i == 1 :
        t.fd(123)


t.end_fill()
