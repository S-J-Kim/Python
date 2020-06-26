R, C = map(int, input().split())
A, B = map(int, input().split())

for s in range(R):

    for p in range(A):

        if s % 2 == 0:
            for i in range(C):
                for j in range(B):
                    if i % 2 == 0:
                        print("X", end='')
                    else:
                        print(".", end='')
        
            print()
        else:
            for i in range(C):
                for j in range(B):
                    if i % 2 == 0:
                        print(".", end='')
                    else:
                        print("X", end='')
        
            print()