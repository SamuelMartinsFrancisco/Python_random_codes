'''
Implemente um programa que comece pedindo ao usuário para digitar uma identificação
de login (ou seja, uma string). O programa, então, verifica se a identificação
informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários
válidos. Dependendo do resultado, uma mensagem apropriada deverá ser impressa. Não
importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
'''

rgstrdUsers = ['joe', 'sue', 'hani', 'sophie'];
login = input('Por favor, digite seu login: ');

if login in rgstrdUsers:
    print('\nVocê entrou!');
else:
    print('\nNão encontramos seu login, que tal se cadastrar?');

print('\nFim');
