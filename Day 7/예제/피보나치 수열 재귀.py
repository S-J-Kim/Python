# 단순 재귀는 시간이 오래 걸린다. 아주 오래 걸린다.

def fibo(n):
    if n == 1 or n == 2: return n
    else: return fibo(n - 1) + fibo(n - 2)

#print(fibo(36))

# 메모화를 통해서 시간 단축

dic = {1: 1, 2: 1}

def fibo_mem(n):
    if n in dic: return dic[n]

    else:
        output = fibo_mem(n - 1) + fibo_mem(n - 2)
        dic[n] = output
        return output   

print(fibo_mem(1000))