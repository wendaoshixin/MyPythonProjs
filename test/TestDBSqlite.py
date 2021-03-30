#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('word.db')
c = conn.cursor()
print ("Opened database successfully")

# CREATE TABLE Book (id integer primary key autoincrement, word text, create_time long, update_time long, delete_flag integer, creator text);

# c.execute("INSERT INTO Book (word,create_time,update_time,delete_flag,creator) VALUES ('zhongwu', 12344556, 32, 1, 'dfsfsf')")
#


with open('关键词.txt', "r", encoding="utf-8") as f:
    for line in f:
        c.execute(f"INSERT INTO Book (word,create_time,update_time,delete_flag,creator) VALUES ('{line}', 12344556, 32, 1, '{line}')")


conn.commit()
print ("Records created successfully")
conn.close()