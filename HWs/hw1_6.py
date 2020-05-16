import re

n = int(input())
phrase = [input() for _ in range(n)]

for m in phrase:
    print("DANGER") if re.fullmatch(r'(100+1+|01)+', m) else print("PASS")