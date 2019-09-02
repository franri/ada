def mid(s, e):
    return (s+e)//2

def binary_search(a, n):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = mid(start, end)
        if a[middle] == n:
            return middle
        elif n < a[middle]:
            end = middle - 1
        elif n > a[middle]:
            start = middle + 1
    return -1