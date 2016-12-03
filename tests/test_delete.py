# -*- coding: utf-8 -*-
import sqlite3, hashlib

con = sqlite3.connect("persona.db")
cur = con.cursor()

#sql = """\
#INSERT INTO pers_data
#    VALUES (
#    NULL,
#    "Иван",
#    "Петров",
#    "Vasily",
#    "Ivanoff",
#    "02.02.1982",
#    "Литва",
#    "0034580",
#    "00234568-011980",
#    "BBB557",
#    "21.06.2013",
#    "Латвия",
#    "Выезд",
#    "Силене",
#    "Таможня",
#    "Фабула",
#    "Сигареты",
#    "пачек",
#    2000,
#    "долларов",
#    2200);
#
#INSERT INTO users (
#    user_id,
#    login,
#    password)
#    VALUES (
#    NULL,
#    "my_admin",
#    "my_password");
#"""

login = "ADMIN"
user_id = 1

sql_req = "DELETE FROM users\
            WHERE login=? AND\
            user_id=?;"
            
sql_arr = (login, user_id)
try:
    cur.execute(sql_req, sql_arr)
except sqlite3.DatabaseError as err:
    print("Ошибка: ", err)
else:
    print("Запрос успешно выполнен")
    con.commit()

cur.close()
con.close()

input()

