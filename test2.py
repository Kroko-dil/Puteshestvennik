from tkinter import *


def printer(event):
    print ("Как всегда очередной 'Hello World!'")
    trxt.configure(text ="Хаха работает!")
def printer2(event):
    print ("Как всегда очередной '22222222'")
    trxt.configure(text="А нет не работает")
def printer3(event):
    print ("Как всегда очередной '22222222'")
    trxt.configure(text="А нет не работает")
    but3.configure(text="Изменено")

root = Tk()
root.title("Удивительное приключение!")   # Название окна
root.geometry('600x400+300+100')                # Размер окна

trxt = Label(root, text="Короче тут должен быть текст", font=("Arial Bold", 25),bg="black", fg="white")  # Текст
trxt.grid(column=10, row=0)              #column - столбец , row - ряд
                                            #bg="black" - цвет фона fg="red" -цвет текста



but = Button(root)          # Создание первой кнопки
but["text"] = "Переход на первый путь"
but.bind("<Button-1>", printer)
but.grid(column=10, row=10)

but2 = Button(root)          # Создание второй кнопки
but2["text"] = "Переход на второй путь"
but2.bind("<Button-1>", printer2)
but2.grid(column=10, row=15)

but3 = Button(root)          # Создание третьей кнопки
but3["text"] = "Переход на третий путь"
but3.bind("<Button-1>", printer3)
but3.grid(column=10, row=20)

root.mainloop()

