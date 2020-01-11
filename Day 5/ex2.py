import random

while True:
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    ans = r1 + r2

    input_ans = input(f'{r1} + {r2} = ')
    
    if int(input_ans) == ans: print("잘했어요!!")
    else: print("다시 해보세요")