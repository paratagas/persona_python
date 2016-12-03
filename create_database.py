# -*- coding: utf-8 -*-

# Создание и подкл базы данных
# Закрыть все окна, вызвать командную строку
# Сменить папку на содержащую sqlite3.exe путем запроса (например)
# cd C:\Python33
# Выполнить запрос:
# sqlite3.exe persona.db

import sqlite3

con = sqlite3.connect("persona.db")
cur = con.cursor()

sql = """\
CREATE TABLE pers_data (
    pers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    sur TEXT,
    name_lat TEXT,
    sur_lat TEXT,
    birth TEXT,
    civil TEXT,
    passport TEXT,
    number_pers TEXT,
    number_auto TEXT,
    date_info TEXT,
    country TEXT,
    direction TEXT,
    ppr TEXT,
    who TEXT,
    fab TEXT,
    sort TEXT,
    quant_sel TEXT,
    quant INTEGER,
    price_sel TEXT,
    price INTEGER,
    date_sys TEXT);

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT);
    
CREATE INDEX index_sur ON pers_data (sur);
CREATE INDEX index_sur_lat ON pers_data (sur_lat);
CREATE INDEX index_passport ON pers_data (passport);
CREATE INDEX index_number_auto ON pers_data (number_auto);
CREATE INDEX index_date_sys ON pers_data (date_sys);
CREATE INDEX index_direction ON pers_data (direction);
CREATE INDEX index_ppr ON pers_data (ppr);
CREATE INDEX index_login ON users (login);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("Ошибка: ", err)
else:
    print("Запрос успешно выполнен")
    con.commit()

cur.close()
con.close()

input()

