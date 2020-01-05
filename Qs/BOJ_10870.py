'''
https://www.acmicpc.net/problem/10870
'''

def fibo(n):
    if n == 2 or n == 1: return 1
    if n == 0: return 0
    
    return fibo(n) + fibo(n - 1)
    
n = int(input())
print(fibo(n))