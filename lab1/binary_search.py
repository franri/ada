def mid(s, e):
    return (s+e)//2

def binary_search(a, n):
    start = 0
    end = len(a)
    middle = mid(start, end)
    while True:
        if a[middle] == n:
            return middle
        if start == end:
            return 'Not Found'
        elif n < a[middle]:
            end = middle - 1
            middle = mid(start, middle)
        elif n > a[middle]:
            start = middle + 1
            middle = mid(middle, end)
