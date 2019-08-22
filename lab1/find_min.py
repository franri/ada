def find_min(a):
    min = a[0]
    index = 0
    for i, el in enumerate(a):
        if el < min:
            min = el
            index = i
    return (index, min)