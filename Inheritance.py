import random

class MyList(list):
    def choice(self):
        return random.choice(self);

differentList = MyList(['Bom', 'dia', '!'])
print(differentList.choice())
