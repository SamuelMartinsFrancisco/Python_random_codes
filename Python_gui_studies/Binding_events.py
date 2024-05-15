from tkinter import Tk, Text

def keyPressed(event):
	print('char:{}'.format(event.keysym))
	
def mouseClickedLeft(event):
	print('mouse left clicked')
	
def mouseClickedRight(event):
	print('mouse right clicked')
	
def mouseClickedMiddle(event):
	print('mouse middle clicked')

root = Tk()
text = Text(root, width=20, height=5)
text.bind('<KeyPress>', keyPressed)
text.bind('<Button-1>', mouseClickedLeft)
text.bind('<Button-2>', mouseClickedMiddle)
text.bind('<Button-3>', mouseClickedRight)
text.pack(expand=True, fill='both')

root.mainloop()


'''
	- O método bind é usado para escutar determinados eventos que ocorrerem sobre um widget;
	- O widget Text cria uma caixa de texto, parecida com o textarea do html;
'''
