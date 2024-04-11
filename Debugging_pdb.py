import pdb

breakpoint()
def h(n):
    breakpoint()
    print('Start h')
    # pdb.run('print(' + str(n) + ')')
    print(1/n)
    print(n)

breakpoint()
def g(n):
    breakpoint()
    print('Start g')
    # pdb.run('print(' + str(n) + ')')
    h(n-1)
    print(n)

breakpoint()
def f(n):
    breakpoint()
    print('Start f')
    # pdb.run('print(' + str(n) + ')')
    g(n-1)
    print(n)

f(2)
h(3)



'''
O comando breakpoint() por si importa o módulo pdb
e chama o pdb.set_trace(); essa é uma forma de iniciar o depurador;

O breakpoint() faz com que o depurador pare e espere
naquele ponto pelo que fazer em seguida; existem muitas
possibilidade quanto ao que fazer, que podem ser encontradas
na documentação;
    - documentação: https://docs.python.org/3/library/pdb.html
    - artigo: https://realpython.com/python-debugging-pdb/

-----------------------------------------------------------------------------

Para experimentar como funciona executar trechos de código separadamente
(separados através do breakpoint), tente usar, na mesma ordem, os comandos:
    > continue
    > jump 28
    > continue
    > continue

-----------------------------------------------------------------------------

Existem duas formas (que conheço) de ver o valor de, por exemplo, uma variável
entre as pausas da depuração:
    - A primeira é colocando o comando
        pdb.run('print(' + str(n) + ')')
    no lugar apropriado diretamente no código;
    - A segunda forma é através do terminal, usando o comando
        p nome_da_variavel
    no momento apropriado

------------------------------------------------------------------------------

O comando ll faz um print do trecho de código todo, que está sendo executado no momento

------------------------------------------------------------------------------

Para experimentar como funciona ver o valor de uma variável em cada momento da execução,
tente usar, na mesma ordem, os comandos:
    > continue
    > continue
    > continue
    > p n
    > continue
    > p n
    > continue
    > p n
'''
