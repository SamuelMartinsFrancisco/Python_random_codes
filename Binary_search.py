import random

numbers = random.sample(range(40), 15)
numbers.sort()

def binarySearch(l, element):
    '''
    Algoritmo de busca binária iterativo
    '''
    
    found = False
    start = 0
    end = len(l)
    middle = end // 2

    print(l, '\n')
    while not found:
        if element == l[middle]:
            found = True
        elif element < l[middle]:
            end = middle
            print('<-')
        elif element > l[middle]:
            start = middle
            print('->')

        middle = start + ((end - start) // 2)
        
        if (middle == start or middle == end) and (element != l[middle]):
            break

    return found      
            

