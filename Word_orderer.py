#Primeiro, execute a atribuição palavras =
#['taco', 'bola', 'celeiro', 'cesta', 'peteca']
#Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a
#primeira e a última palavras em palavras, na ordem do dicionário.

words = ['taco', 'bola', 'zebra', 'jacaré', 'celeiro', 'lagarto', 'cesta', 'peteca', 'abelha'];
words_len = len(words);

words_index_hierarchy = [""] * words_len;
def orderer(words_list):
    for i in range(0, words_len):
        isHigherThan = 0;
        for l in range(0, words_len):
            if words_list[i] > words_list[l]:
                isHigherThan = isHigherThan + 1;  
            if l == words_len - 1:
                words_index_hierarchy[isHigherThan] = words_list[i];
            
    return words_index_hierarchy;
    
def show_list():
    text = "\nWords list organized in dictionary order: \n";
    for word in orderer(words):
        text += "\n   * " + word;
    return print(text);

print('\nGiven list:', words);
show_list();

