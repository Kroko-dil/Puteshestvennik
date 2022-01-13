import sqlite3
import sys
from tkinter import *


class BD:
    sqlite_connection = sqlite3.connect('БД v0.01.db')
    print("База данных создана и успешно подключена к SQLite")
    cursor = sqlite_connection.cursor()
    cursorr = sqlite_connection.cursor()
    cursor.execute("SELECT * FROM Poit")
    print(cursor.fetchall())
    def f(self):
        self.cursor.execute("SELECT * FROM Poit")
        print(self.cursor.fetchall())


class perehod:

    def __int__(self, steppp, reb, rebro1, rebro2, rebro3,cek):
        self.steppp = steppp
        self.reb = reb
        self.rebro1 = rebro1
        self.rebro2 = rebro2
        self.rebro3 = rebro3
        self.cek=cek

    def poik_reb(self, cur):
        print(" Начало поиска количества ребер у вершины")
        cur.cursor.execute("SELECT * FROM Poit")
        while 1:
            self.records = cur.cursor.fetchmany(1)
            for r in self.records:
                rg = r[1]
            print(r[1], "dfghdccc")
            if r[1] == 11: break
            if r[1] == self.steppp:
                hotu.reb = r[2]

    def zap_list(self, cur):
        print(" Запись на лист")
        cur.cursor.execute("SELECT * FROM Poit")
        print(self.records)
        while 1:
            self.records = cur.cursor.fetchmany(1)
            for r in self.records:
                rg = r[1]
            #print(r[1], "Проверка на листе")
            if r[1] == self.steppp:
                trxt.delete("1.0", END)
                trxt.insert(INSERT, r[3])
                #print(self.records)
                break

    def zap(self, step, reb, cur):
        print(" Начало смены названий кнопок")
        cur.cursor.execute("SELECT * FROM roads")


        print(reb, '   ребра')
        if reb == 3:
            print("заполнилась первая кнопка ")
            print(step, '   точка')
            cur.cursor.execute("SELECT * FROM roads")

            for i in range(3):
                print(i)
                while 1:
                    self.records = cur.cursorr.fetchmany(1)
                    print("Перебор 33333")
                    for r in self.records:
                        rg = r[1]
                    print(r[1],step, "df333333gh")
                    print(self.records)
                    #if r[1] == 11: break
                    if r[1] == step:
                        if i == 0:
                            but1.configure(text=r[3])
                            self.rebro1 = r[2]
                        elif i == 1:
                            but2.configure(text=r[3])
                            self.rebro2 = r[2]
                        else:
                            but3.configure(text=r[3])
                            self.rebro3 = r[2]
                            print(" Конец заполнению кнопок")
                        break
        elif reb == 2:
            cur.cursor.execute("SELECT * FROM roads")
            print(step, '   точка')
            for i in range(2):
                print(i)
                j = 0
                while j != 1:
                    self.records2 = cur.cursorr.fetchmany(1)
                    print("Перебор 22222")
                    for r in self.records2:
                        rg = r[1]
                    print(r[1],step, "df2222gh")
                    if r[1] == 11: break
                    if r[1] == step:
                        if i == 0:
                            but1.pack()
                            but1.configure(text=r[3])
                            self.rebro1 = r[2]
                            j = j + 1
                        elif i == 1:
                            j = j + 1
                            but2.pack()
                            but2.configure(text=r[3])
                            self.rebro2 = r[2]
                            self.rebro3 = 0
                            but3.pack_forget()
                            print(" Конец заполнению кнопок")
        elif reb == 1:
            cur.cursor.execute("SELECT * FROM roads")
            print(step, '   точка')
            print(self.steppp, '    точка глобал')
            j = 0
            while j != 1:
                self.records = cur.cursor.fetchmany(1)
                for r1 in self.records:
                    print(r1[1],step, "df111gh")
                if r1[1] == step:
                    j = j + 1
                    but1.pack()
                    print(r1[3], "  fghfghfgh")
                    but1.configure(text=r1[3])
                    but2.pack_forget()
                    but3.pack_forget()
                    self.rebro1 = r1[2]
                    self.rebro2 = 0
                    self.rebro3 = 0
                    self.steppp=r1[2]
                    print(self.steppp, ' точка глобал проверка')
                    print(" Конец заполнению кнопок")
                    if r1[3]=='Конец':
                        self.cek=1

                    break
                if r1[1] == 11: break

    def nachalo(self, cur, curr):
        cur.cursor.execute("SELECT * FROM Poit")
        curr.cursorr.execute("SELECT * FROM roads")
        print("Началось")

        self.steppp = 1
        step = self.steppp
        self.records = cur.cursor.fetchmany(1)
        for r in self.records:
            rg = r[1]
        trxt.insert(INSERT, r[3])
        self.zap(step, r[2], curr)

    def perexod(self, cur, step):
        cur.cursor.execute("SELECT * FROM roads")
        #   Считывание из БД
        self.records = cur.cursor.fetchmany(1)
        print("Всего строк:  ", len(self.records))
        print("Вывод каждой строки")
        print(self.records)
        print("Вывод каждой строки")
        for row in self.records:
            print("ID:", row[0])
            print("Начало:", row[1])
            print("Конец:", row[2])
            print("Текст:", row[3])
            print("Дополнительно:", row[4], end="\n\n")
            s = row[1]
        trxt.insert(INSERT, s)

hotu = perehod()
bbb = BD()

def Start_game(event):
    but.destroy()
    print("vsdj")
    trxt.pack(side=LEFT)
    scroll.pack(side=LEFT, fill=Y)
    print("vsdjrgfhfh")
    but1.pack()
    but2.pack()
    but3.pack()
    # trxt.configure(command=hotu.nachalo(bbb,bbb))
    hotu.nachalo(bbb, bbb)
    hotu.cek=0

def Game_over():
    but4.pack(anchor=CENTER, expand=1)
    but1.pack_forget()
    but2.pack_forget()
    but3.pack_forget()
    but.destroy()
    trxt.pack_forget()
    scroll.pack_forget()


def printer(event):
    if hotu.steppp==11:
        Game_over()
    else:
        print(" Нажатие первой кнопки")
        cur = bbb.cursor
        hotu.steppp = hotu.rebro1
        hotu.poik_reb(bbb)
        print(hotu.reb,)
        hotu.zap(hotu.rebro1, hotu.reb, bbb)    #Запись на кнопки
        hotu.zap_list(bbb) #Запись на лист
        print("    Конец нажатию кнопки")


def printer2(event):
    print("Как всегда очередной '22222222'")
    cur = bbb.cursor

    hotu.steppp = hotu.rebro2
    hotu.poik_reb(bbb)
    print(hotu.reb, 'ffffffffffffffffffffffffffffffff')
    hotu.zap(hotu.rebro2, hotu.reb, bbb)
    hotu.zap_list(bbb)


def printer3(event):
    print("Как всегда очередной '22222222'")
    cur = bbb.cursor
    hotu.steppp = hotu.rebro3
    hotu.poik_reb(bbb)
    print(hotu.reb, 'ffffffffffffffffffffffffffffffff')
    hotu.zap(hotu.rebro3, hotu.reb, bbb)
    hotu.zap_list(bbb)

def printer4(event):
    sys.exit()


root = Tk()
root.title("Удивительное приключение!")  # Название окна
root.geometry('600x400+300+100')  # Размер окна
root.resizable(width=False, height=False)

trxt = Text(root, width=20, height=10, font=("Arial Bold", 25), wrap=WORD)  # Текст
# column - столбец , row - ряд  bg="black" - цвет фона fg="red" -цвет текста

scroll = Scrollbar(command=trxt.yview)
trxt.config(yscrollcommand=scroll.set)

but = Button(root)  # Создание первой кнопки
but["text"] = "Начал истории"
but["height"]=10
but["width"]=30
but.bind("<Button-1>", Start_game)
but.pack(anchor=CENTER, expand=1)


but1 = Button(root)  # Создание первой кнопки
but1["text"] = "Переход на первый путь"
but1["wraplength"] = 205
but1.bind("<Button-1>", printer)

but2 = Button(root)  # Создание второй кнопки
but2["text"] = "Переход на второй путь"
but2["wraplength"] = 205
but2.bind("<Button-1>", printer2)

but3 = Button(root)  # Создание третьей кнопки
but3["text"] = "Переход на третий путь"
but3["wraplength"] = 205
but3.bind("<Button-1>", printer3)

but4 = Button(root)  # Создание конечной кнопки
but4["text"] = "Конец истории"
but4["wraplength"] = 205
but["height"] = 10
but["width"] = 30
but4.bind("<Button-1>", printer4)

root.mainloop()

