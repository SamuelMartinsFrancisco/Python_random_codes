from tkinter import Tk, Label

root = Tk()

for r in range(4):
    for c in range(3):
        label = Label(root, borderwidth=2, relief='solid', bg='#fce', width=25, height=10)
        label.grid(row=r, column=c)

root.mainloop()
