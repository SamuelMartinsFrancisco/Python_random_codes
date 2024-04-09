'''
Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa
(em metros) e o peso (em quilos) e calcula o Índice de Massa Corporal (IMC)
dessa pessoa. 
Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5,
'Normal' se 18,5 <= imc < 25, e
'Sobrepeso' se imc >= 25.
'''

print('*** Esse programa é um calculador de índice de massa corporal ***\n');

weight = eval(input('Por favor, digite seu peso (kg): '));
height = eval(input('Agora, digite sua altura (m): '));

def imc(w, h):
    '''
        Essa função calcula o IMC e retorna informações a respeito dele.
        Os parâmetros da função são: peso e altura,
        nessa ordem; 
    '''
    
    result = weight / (height**2);

    print('\n\nPeso: ', str(round(weight, 2)) + 'kg');
    print('Altura: ', str(round(height, 2)) + 'm');
    print('Índice de massa corporal: ', round(result, 2));

    print('\nEstado da relação entre seu peso e sua altura:')
    if result < 18.5:
        print(' - Abaixo do peso');
    elif result >= 18.5 and result < 25:
        print(' - Normal');
    elif result > 25:
        print(' - Sobrepeso');

    return result;

imc(weight, height);
