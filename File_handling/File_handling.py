
def fileHandling(path):
    file = open(path, 'r')
    content = file.read()
    content = content.strip()
    
    if len(content) > 10:
        print('No arquivo há mais de 10 letras, números, ou símbolos')
        return content
    else:
        print('O arquivo está quase vazio!')
        text = input('Escreva algo nele nesse caso: ')
        file = open(path, 'w')
        file.write(text)
        file.close()


fileHandling('file.txt')
