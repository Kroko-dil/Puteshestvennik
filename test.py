import sqlite3

try:
    sqlite_connection = sqlite3.connect('БД v0.01.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    cursor.execute("SELECT * FROM roads")
    #print("Тут чтото должно быть", cursor.fetchmany(1))

    records = cursor.fetchmany(1)
    records = cursor.fetchmany(1)
    records = cursor.fetchmany(1)
    records = cursor.fetchmany(1)
    print(records)
    cursor.execute("SELECT * FROM roads")
    records = cursor.fetchmany(0)
    print(records)
    records = cursor.fetchmany(0)
    print(records)
    cursor.execute("SELECT * FROM roads")
    records = cursor.fetchall()
    print(records)

    records = cursor.fetchone()
    #print(records)
    records = cursor.fetchmany(-1)
    #print (records)
    #for row in records:
        #print("ID:", row[0])


    cursor.close()
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT * FROM Poit")
    records = cursor.fetchmany(1)

    for row in records:
        print("ID:", row[0])


    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")