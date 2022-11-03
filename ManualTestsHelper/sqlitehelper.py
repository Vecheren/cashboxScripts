import sqlite3
from helpers import fileshelper
from helpers import nethelper
import os

dbPath = os.path.join(fileshelper.findCashboxPath(), "db", "db.db")

try:
    connect = sqlite3.connect(dbPath)
    cursor = connect.cursor()
    
    query = "select * FROM CashboxState"
    cursor.execute(query)
    record = cursor.fetchall()
    print(record[0][1])
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connect):
        connect.close()
        print("Соединение с SQLite закрыто")