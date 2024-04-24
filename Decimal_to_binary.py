class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return not len(self.data) > 0


def dec2bin(num):
    p = Pilha()

    while num > 0:
        rest = num % 2
        num = num // 2
        p.push(str(rest))
        
        if num == 1:
            num = 0
            p.push('1')

    binary = p.data
    binary.reverse()
    binary = ''.join(binary)
    
    return binary

