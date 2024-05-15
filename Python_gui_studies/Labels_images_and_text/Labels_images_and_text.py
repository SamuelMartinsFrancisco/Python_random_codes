from tkinter import Tk, Label,PhotoImage, RIGHT
from PIL import ImageTk, Image

root = Tk()
msg = 'Hey! :)'
msg2 = 'Yuup! :D'
img = ImageTk.PhotoImage(Image.open('img.jpg').resize((600, 400)))

labelText = Label(master=root, font=('Comic Sans MS', 16), text=msg)
labelImage = Label(master=root, image=img)
labelText2 = Label(master=root, bg='#fe3', padx=20, text=msg2)

labelText.pack()
labelImage.pack()
labelText2.pack(side=RIGHT)

root.mainloop()

'''
    - O método mainloop, sozinho, cria uma janela vazia;
    - A classe Label é um tipo de widget, e serve para criar um elemento (um texto, uma imagem, ...)
que pode ser inserido na janela;
    - A inserção de fato, é feita pelo método pack()
    - A disposição dos elementos pode ser trabalhada através do módulo geometry manager, que faz parte do tkinter
    - Quanto a alguns parâmetros do Label:
        - bg é usado para definir a cor de fundo;
        - fg é usado para definir a cor da fonte (a cor interna do elemento);
        - padx e pady se referem ao padding do elemento;
    - Os elementos também podem ser posicionados por meio do método grid()
'''
