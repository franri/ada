import numpy as np

def trip(m):
    
    r = np.copy(m)

    # guardo [costo, origen]
    min_for_each_city = [[1000, None] for _ in range(r.shape[0])]
    # calculo costo de llegar a cada ciudad i viniendo de ciudad j (acumulo los costos)
    # j es columnas, i es filas. Guardo el mínimo en array aux
    for j in range(r.shape[0]):
        min_for_each_city[j] = [r[0][j], 0]
        for i in range(j):
            r[i][j] = r[i][j] + min_for_each_city[i][0]
            if r[i][j] < min_for_each_city[j][0]:
                min_for_each_city[j] = [r[i][j], i]
    # Ahora, tengo el minimo para llegar a cada ciudad, y de donde,
    # en el segundo lugar de min ultima ciudad tengo el origen de esa ciudad

    stack = []
    i = min_for_each_city[-1][1]
    stack.append(len(min_for_each_city)) # la ultima ciudad
    stack.append(i+1) # como llego a la ultima ciudad
    while i>0:
        i = min_for_each_city[i][1]
        stack.append(i+1)

    costo = min_for_each_city[-1][0]
    stack.reverse()

    print("Costo: ", costo)
    print("Ciudades: ", stack)

    return costo, stack
