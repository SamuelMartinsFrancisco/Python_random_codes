def transposedMatrix(m):
    n_rows = len(m)
    n_columns = int()
    result = [];

    for row in range(0, n_rows):
        result.append(list())
        n_columns = len(m[row])
        
        for column in range(0, n_columns):
            result[row].append(m[column][row])
    
    return result


l = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]
    
if l == transposedMatrix(l):
    print('\nAfinal, a matriz que você inseriu é simétrica a sua transposta!')
else:
    print('\nA matriz inserida e a sua transposta não são simétricas.')

print(transposedMatrix(l))
