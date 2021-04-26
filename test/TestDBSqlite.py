#!/usr/bin/python

import sqlite3




def insert():
     conn = sqlite3.connect('word.db')
     c = conn.cursor()
     print("Opened database successfully")

     # CREATE TABLE Book (id integer primary key autoincrement, word text, create_time long, update_time long, delete_flag integer, creator text);

     # c.execute("INSERT INTO Book (word,create_time,update_time,delete_flag,creator) VALUES ('zhongwu', 12344556, 32, 1, 'dfsfsf')")
     #

     with open('关键词.txt', "r", encoding="utf-8") as f:
          for line in f:
               c.execute(
                    f"INSERT INTO Book (word,create_time,update_time,delete_flag,creator) VALUES ('{line}', 12344556, 32, 1, '{line}')")

     conn.commit()
     print("Records created successfully")
     conn.close()

def queryData():
     # 创建连接
     con = sqlite3.connect('word.db')
     # 创建游标对象

     cur = con.cursor()
     # 创建查询sql
     sql = 'select * from Book'
     try:
          cur.execute(sql)
          # 获取结果集合
          person_all = cur.fetchall()
          # print(person_all)
          # [(1,'张三',24), (2,'小李',23), (3,'小花',34), (4,'小明',28)]
          for person in person_all:
               print(person)
     except Exception as e:
          print(e)
          print("查询数据失败")
     finally:
          # 关闭游标
          cur.close()
          # 关闭连接
          con.close

if __name__ == '__main__':
     # insert()
     queryData()