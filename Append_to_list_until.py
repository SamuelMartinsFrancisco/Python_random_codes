thingsList = [];
item = input('Digite uma coisa qualquer: ');

while item != '':
    thingsList.append(item);
    item = input('Digite uma coisa qualquer: ');

for item in thingsList:
    print(item);

