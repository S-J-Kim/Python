li = list(map(int, input().split()))
tmp = [0 for i in range(len(li))]

def merge(low, mid, high):
    i = low; j = mid + 1; k = low

    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp[k] = li[i]
            i += 1
        
        else:
            tmp[k] = li[j]
            j += 1

        k += 1

    if i > mid:
        for i in range(j, high + 1):
            tmp[k] = li[j]
            k += 1
        
    else:
        for i in range(i, mid + 1):
            tmp[k] = li[i]
            k += 1
    
    for i in range(low, high + 1):
        li[i] = tmp[i]

def MergeSort(low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(low, mid)
        MergeSort(mid + 1, high)
        merge(low, mid, high)


MergeSort(0, len(li) - 1)
print(li)