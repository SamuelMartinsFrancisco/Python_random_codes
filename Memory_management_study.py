# Tipos mutáveis e não mutáveis

'''
    Atribuir uma variável como valor a outra variável faz com que elas se
    refiram a um mesmo objeto;
'''


# Quando se altera o valor de uma variável de tipo imutável, é criado um novo
# objeto, a quem ela passa a se referir

numeroPessoas = 6
numeroAraras = numeroPessoas

numeroPessoas = 5

print('\nnúmero de araras:', numeroAraras)
print('número de pessoas:', numeroPessoas)



# O tipo list é um tipo mutável, isto é, que pode ter seu conteúdo alterado,
# e por isso um novo objeto não precisa ser criado, e as duas variáveis
# permanecem apontando para o mesmo objeto

estojo = ['lápis','borracha','tesoura']
outroEstojo = estojo

outroEstojo.append('cola')

print('\n      estojo:', estojo)
print('outro estojo:', outroEstojo)
