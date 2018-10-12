try:
    from tkinter import *
except ImportError as ex:
    from Tkinter import * # python 2

choices = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet']

class Form(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar()
        for key in choices:
            Radiobutton(self, text=key,
                              command=self.onPress,
                              variable=self.var,
                              value=key).pack(anchor=NW)
        self.var.set(key)
        Button(self, text='State', command=self.report).pack(fill=X)
        Button(self, text='Quit', command=self.exit).pack(fill=X)
        Button(self, text='Rumpa', command=self.stuff).pack(fill=Y)
    def exit(self):
        self.quit()
    def stuff(self):
        print("RUMPA")
    def onPress(self):
        pick = self.var.get()
        print('You pressed {}'.format(pick))
    def report(self):
        print(self.var.get())

Form().mainloop()


