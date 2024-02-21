#Ler uma temperatura em graus Celsius e apresentá-la convertida
#em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
#sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

print("Esse é um conversor de celsius para farenheit.");
celsius = input("Digite a temperatura, em graus Celsius: ");
farenheit = int(celsius) * 9 / 5 + 32;
print("A temperatura informada, em graus farenheit é: " + str(farenheit));
