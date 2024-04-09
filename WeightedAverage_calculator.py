n1 = eval(input('\nInforme a primeira nota: '));
n2 = eval(input('Informe a segunda nota: '));

def calcAverage(n1, n2):
    average = (0.4 * n1) + (0.6 * n2);
    roundedAverage = round(average, 1)
    print('\n -- A média ponderada do estudante é:', roundedAverage);
    return roundedAverage;

def isStudentApproved(avrg):
    if avrg < 5:
        print('\n\nO estudante não está aprovado.');
    else:
        print('\n\nO estudante está aprovado.');

isStudentApproved(calcAverage(n1, n2));
