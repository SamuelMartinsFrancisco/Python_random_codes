import time

class Queue:
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if not self.empty():
            return self.data.pop(0)

    def empty(self):
        return not len(self.data) > 0

    def next(self):
        if not self.empty():
            return self.data[0]


normal = Queue()
priority = Queue()

def getInLine(person, age):
    if age > 60:
        priority.insert(person)
    else:
        normal.insert(person)
    

def beginService():
    start = time.time()
    serviceOrder = 2
    counter = 0

    print('\n\n')
    print('Fila normal:', normal.data)
    print('Fila prioritária:', priority.data, '\n')

    while not normal.empty() or not priority.empty():
        if priority.empty():
            counter += 1
            print(counter,  '-', normal.next())
            normal.remove()
        else:
            while serviceOrder > 0:
                counter += 1
                print(counter,  '-', priority.next())
                priority.remove()
                serviceOrder -= 1
                if priority.empty():
                    serviceOrder = 0
            counter += 1
            print(counter,  '-', normal.next())
            normal.remove()
            serviceOrder = 2
    

getInLine('samuel', 19)
getInLine('josefino', 91)
getInLine('rodolfo', 45)
getInLine('lourdes', 67)
getInLine('lourdes', 67)
getInLine('lous', 67)
getInLine('lodes', 67)
getInLine('baraquias', 15)
beginService()
