# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("persona.db")
cur = con.cursor()


#SELECT * FROM info;
#SELECT * FROM tmc;
#SELECT * FROM users;

sql = """\
SELECT * FROM pers_data;
"""
sql_2 = """\
SELECT * FROM users;
"""

try:
    cur.execute(sql)
    arr = cur.fetchall()
    print(arr)
    cur.execute(sql_2)
    arr_2 = cur.fetchall()
    print(arr_2)
    
except sqlite3.DatabaseError as err:
    print("Ошибка: ", err)
else:
    print("Запрос успешно выполнен")
    con.commit()

cur.close()
con.close()

input()

