import sqlite3

connection = sqlite3.connect("database/reuse_smart.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM barang")

data = cursor.fetchall()

for barang in data:
    print(barang)

connection.close()