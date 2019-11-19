import numpy as np
import matplotlib.pyplot as plt
import random
import time

from binary_search import binary_search
from find_min import find_min
from selection_sort import selection_sort

max = 100

inputs = [10000 + 10000*i  for i in range(0, max)]

def bs():
    bs_a = [None]*len(inputs)

    for i, n in enumerate(inputs):
        print('llegue aca adentro', i)
    
        array_to_search = [1]*n
        print(len(array_to_search))
        start = time.time()
        binary_search(array_to_search,-1)
        end = time.time()
        print(start)
        print(end)
        resta = end - start
        bs_a[i] = resta

    print(bs_a)
    plt.plot(inputs, bs_a)
    plt.xlabel('Inputs')
    plt.ylabel('"Time"')
    plt.title('Binary Search')
    plt.show()
    

def fm():
    fm_a = [None]*len(inputs)

    for i, n in enumerate(inputs):
        print('llegue aca adentro', i)
    
        array_to_search = [1]*n
        print(len(array_to_search))
        start = time.time()
        print(start)
        find_min(array_to_search)
        end = time.time()
        print(end)
        resta = end - start
        fm_a[i] = resta

    print(fm_a)
    plt.plot(inputs, fm_a)
    plt.xlabel('Inputs')
    plt.ylabel('"Time"')
    plt.title('Find Min')
    plt.show()
    
    
def ss():
    
    step = 2000
    entradas = [1750 + step*i for i in range(1, 10)]
    print(entradas)
    # entradas.append()

    ss_a = [None]*len(entradas)
    
    for i, n in enumerate(entradas):
        print('llegue aca adentro', i)
    
        array_to_sort = [i for i in range(n, 0, -1)]
        print(len(array_to_sort))
        start = time.time()
        selection_sort(array_to_sort)
        end = time.time()
        print(start)
        print(end)
        resta = end - start
        ss_a[i] = resta

    print(ss_a)
    plt.plot(entradas, ss_a)
    plt.xlabel('Inputs')
    plt.ylabel('"Time"')
    plt.title('Selection Sort')
    plt.show()

def bs_a_mano():
    inputs = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9]
    times = [None]*len(inputs)
    for i, n in enumerate(inputs):
        print(n)
        arr = [1]*n
        start = time.time()
        binary_search(arr, -1)
        end = time.time()
        resta = end - start
        times[i] = resta
        print(resta)
    plt.plot(times)
    plt.xlabel('Inputs')
    plt.ylabel('"Time"')
    plt.title('Binary Search')
    plt.show()

    

if __name__ == '__main__':
    # ss()
    # fm()
    # bs()
    bs_a_mano()

# arr = [1]*1000000000

# start = time.time()
# binary_search(arr,1)
# end = time.time()
# print(start)
# print(end)
# resta = end - start
# print(resta)