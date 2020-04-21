li = list(map(int, input().split()))

def Partition(low, high):
    pivot = low
    i = low + 1
    j = high

    while i <= j:
        while li[pivot] >= li[i] and i < j: i += 1
        while li[pivot] < li[j] and i <= j: j -= 1
        
        if i < j: li[i], li[j] = li[j], li[i]
        else: break

    li[pivot], li[j] = li[j], li[pivot]
    return j
    

def QuickSort(low, high):
    if (low < high):
        pivot = Partition(low, high)
        QuickSort(low, pivot - 1)
        QuickSort(pivot + 1, high)

QuickSort(0, len(li) - 1)
print(li)
        
