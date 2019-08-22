from find_min import find_min

def selection_sort(a):
    current = 0
    while current < len(a):
        i, n = find_min(a[current:])
        i += current
        if n < a[current]:
                ph = a[current]
                a[current] = n
                a[i] = ph
        current += 1