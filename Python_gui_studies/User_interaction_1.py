from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime

root = Tk()

def showTime():
	time = strftime('Data: %d %b %Y\nHorário: %H:%M:%S %p\n', localtime())
	print(time)
	# showinfo(message=time)

click_here = Button(root, text='Clique aqui', command=showTime)
close_window = Button(root, text='Fechar janela', command=root.quit, bg='#e22', fg='#fff')

close_window.pack()
click_here.pack()

root.mainloop()
