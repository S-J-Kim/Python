li = list(map(int, input().split()))

def Partition(li, low, high):
    pivot = low
    i = low + 1
    j = high
    
    while i < j:
        while li[pivot] > li[i] and i < high: i += 1
        while li[pivot] < li[j] :j -= 1
        
        if i<j:  li[i], li[j] = li[j], li[i]
    
    li[pivot], li[j] = li[j], li[pivot]
    
    

    return j
    

def QuickSort(li, low, high):
    if (low < high):
        pivot = Partition(li, low, high)
        QuickSort(li, low, pivot - 1)
        QuickSort(li, pivot + 1, high)

QuickSort(li, 0, len(li) - 1)
print(li)
        
