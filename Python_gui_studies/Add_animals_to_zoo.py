from tkinter import Tk, Button, Entry, Label

root = Tk()
animals = []

def addAnimal():
	global animals
	global entry
	animal = entry.get()
	
	if animal != '':
		animals.append(animal)
		
	entry.delete(0, 'end') # this resets entry value

def showAnimals():
	global animals
	
	if len(animals) != 0:
		print(animals)
	else:
		print('Parece que o zoológico ainda está vazio')

button = Button(root, text="Adicionar ao zoo", bg='#abc', command=addAnimal)
button_2 = Button(root, text='Ver animais do zoo', command=showAnimals)
entry = Entry(root)
title = Label(root, font=('Georgia', 15), text='Zoológico')
description = Label(root, text='Digite o nome de algum animal e clique no botão.')

title.pack()
description.pack()
button.pack()
entry.pack()
button_2.pack()


root.mainloop()
