# Estudos de Programação Orientada a Objetos
#   Entidade: ponto do plano cartesiano;

class Point:
    '''
        Quando um objeto é instanciado, o método __init__ é chamado automaticamente;
        Esse método também é chamado de método construtor;
        O parâmetro self se refere ao próprio objeto que está sendo instanciado;
    '''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        ''' x e y = 0 é um valor padrão, caso não seja informado outro na criação do objeto; '''

    ''' O método __repr__ serve para definir o que retornar quando o objeto é chamado '''
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, offsetx = 0, offsety = 0):
        self.x += offsetx
        self.y += offsety


''' Dessa forma é feita a instância de um objeto e o uso de seus métodos: '''
point_1 = Point()
point_1.setx(5)
point_1.sety(4)
print(point_1.get())
point_1.move(5, 1)

point_2 = Point(1, -1)
