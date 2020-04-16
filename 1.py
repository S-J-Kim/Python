class lec:
    def __init__(self, num, start, end):
        self.num = num
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start


num_of_lectures = int(input())
lectures = []
for i in range(num_of_lectures):
    tmp = list(map(int, input().split()))
    tmplec = lec(tmp[0],tmp[1],tmp[2])
    lectures.append(tmplec)
lectures = sorted(lectures)
resarr = []
res = 0


def is_ok(arr, lec):
    for i in arr:
        if (i.start < lec.start < i.end) or (i.start < lec.end < i.end):
            return False
    return True


def search(arr, idx):
    global num_of_lectures
    global lectures
    global res
    global resarr
    if idx > num_of_lectures:
        return
    if idx == num_of_lectures:
        if res < len(arr):
            res = len(arr)
            resarr = [0]
            for i in range(len(arr)):
                resarr.append(arr[i])
    tmplist = []
    for i in arr:
        tmplist.append(i)

    if len(arr) == 0:
        tmplist.append(lectures[idx])
        search(tmplist, idx + 1)

    elif is_ok(tmplist, lectures[idx]):
        tmplist.append(lectures[idx])
        search(tmplist, idx + 1)
    tmplist2 = []
    for i in arr:
        tmplist2.append(i)
    search(tmplist2, idx + 1)


tmp = []
search(tmp, 0)
print(res, end="\n")
for i in range(len(resarr)):
    print(resarr[i].num, end=" ")