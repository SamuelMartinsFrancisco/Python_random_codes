p = "((())()()()("
p_size = len(p)

counter = 0
for char in p:
    if char == '(':
        counter += 1
    elif char == ')':
        counter -= 1

if counter == 0:
    print('Tudo certo!')
elif counter > 0:
    print('Faltam', counter, 'parênteses de fechamento')
elif counter < 0:
    print('Faltam', counter*(-1), 'parênteses de abertura')
        
