from urllib.request import urlopen
from html.parser import HTMLParser


'''
A função urlopen() permite fazer uma requisição HTTP a algum servidor;
'''
def getSource(url):
    response = urlopen(url)
    content = response.read()
    
    return content.decode()

html = getSource('https://www.google.com/')



'''
 O módulo parser permite fazer o processamento de um texto HTML;
 Internamente, há um handler para os dados e para cada tipo de tag;
     - Por padrão os handlers não fazem; estão abertos às funcionalidades que podem ser atribuídas a eles
       (quando encontrarem o elemento html correspondente);
           - Essas funcionalidades podem ser implementados criando uma subclasse de HTMLParser e sobrescrevendo os respectivos métodos;
'''

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # imprime todos os links que houver nas tags <a> do documento
        if tag == 'a':
            for atrr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = HTMLParser()
parser.feed(html)
