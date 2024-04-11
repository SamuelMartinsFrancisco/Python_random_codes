
def readFile(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    
    return content

def rewriteFile(path, content = str()):
    file = open(path, 'w')
    file.write(content)
    file.close()

def addToFile(path, content = str()):
    file = open(path, 'a')
    file.write(content)
    file.close()

def fileHandling(path):
    fileLen = len(readFile(path))
    print('Conteúdo inicial: ' + readFile(path) + '\n')
    
    if fileLen < 10:
        print('O arquivo parece meio vazio, olhe só quantas teias de aranha!')
        text = input('Pois então escreva mais algo nele: ')
        addToFile(path, text)
        print('\nBem melhor :D\n', readFile(path))
    else:
        rewrite = input('Gostaria de reescrever o arquivo? (digite "s" ou "n")')
        if rewrite == 's':
            text = input('Pois então digite o novo conteúdo: ')
            rewriteFile(path, text)
            print('\nO arquivo foi reescrito!\n', readFile(path))
            


fileHandling('file.txt')
