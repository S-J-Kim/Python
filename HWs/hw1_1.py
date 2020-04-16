li = list(map(int, input().split()))
n = int(input())

def BS(x, s, e):
    m = (s + e) // 2
    if li[m] == x: return m + 1
    if s == e or s < 0 or e < 0: return None
    
    if x > li[m]: return BS(x, m + 1, e)
    elif x < li[m]: return BS(x, s, m - 1)
    
print(BS(n, 0, len(li)))
