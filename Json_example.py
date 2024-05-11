import json

recipe = dict()

recipe['ingredients'] = ['ovos', 'trigo', 'açúcar', 'leite', 'milho']
recipe['time'] = '45min'
recipe['portions'] = 5


jsonRecipe = json.dumps(recipe, sort_keys=True, indent=4)
decodedJsonRecipe = json.loads(jsonRecipe)


print(jsonRecipe, '\n')
print('json.dumps type:', type(jsonRecipe))
print('json.load type:', type(decodedJsonRecipe))


'''
Este é um exemplo de como funciona o processamento de dados em formato JSON;
O JSON é um tipo de texto, escrito seguindo um padrão específico;
Para que um JSON possa ser devidamente manipulado, ele precisa ser convertido
para outro formato; no caso acima foi convertido em um objeto do tipo dict;
'''
