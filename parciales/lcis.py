def lcis(a):
    cache = [ 'lala' for el in a ]
    cache[0] = [a[0]]
    max_sub = cache[0]
    for i, el in enumerate(a[1:], 1):
        nueva = []
        changed = False
        for lista in cache[0:(i-1)+1]:
            if lista[-1] < el:
                nueva = lista[:]
                nueva.append(el)
                changed = True
        if not changed:
            nueva.append(el)
        cache[i] = nueva
        if len(nueva) > len(max_sub):
            max_sub = nueva
    return max_sub

a = [ 1, 20, 3, 7, 40, 8, 9]
print(lcis(a))