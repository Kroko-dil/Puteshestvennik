import tkinter as tki

class MyApp(object):

    def __init__(self, root_win):
        self.root_win = root_win
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tki.Frame(self.root_win)
        self.frame1.pack()
        self.btn1 = tki.Button(self.frame1, text='I\'m a button')
        self.btn1.pack()
        self.btn1.visible=False #This doesnt't work

def main():
    root_win = tki.Tk()
    my_app = MyApp(root_win)
    root_win.mainloop()

if __name__ == '__main__':
    main()