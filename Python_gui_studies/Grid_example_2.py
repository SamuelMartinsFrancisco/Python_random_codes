from tkinter import Tk, Label

root = Tk()
labels = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]

for r in range(4):
    for c in range(3):
        label = Label(root, borderwidth=5, relief='groove', padx=10, font=('Georgia', 20), text=labels[r][c])
        label.grid(row=r, column=c)

root.mainloop()

'''
    O parâmetro relief define o estilo da borda;
'''



