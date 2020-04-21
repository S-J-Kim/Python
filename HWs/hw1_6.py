import re

n = int(input())
phrase=[input() for _ in range(n)]

p = re.compile(r'(100+1+|01)+')

for m in phrase:
    if p.fullmatch(m): print("DANGER")
    else: print("PASS")