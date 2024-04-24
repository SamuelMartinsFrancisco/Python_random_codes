'''
Essas podem não ser as melhores situações de uso da recursão,
afinal o mesmo pode ser feito de através um laço;
mas é um bom exemplo para entender como essa ferramenta funciona;
'''

def showList(l, i=0):
    if i < len(l):
        print(l[i])
        showList(l, i+1)

def fatorial(n):
    if n == 0:
        return 1
    else:
        result = n * fatorial(n-1)
        return result
