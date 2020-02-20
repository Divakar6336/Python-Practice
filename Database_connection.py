import sqlite3 
from sqlite3 import Error
import json


class Database:
    def _init_(self):
        try:
            conn=sqlite3.connect("EMP_INFO")
            cur=conn.cursor()
            cur.execute("DROP TABLE IF EXISTS salary;")
            cur.execute("CREATE TABLE salary (name vachar, salary integer) ")
            cur.execute("CREATE UNIQUE INDEX moves on salary(name, salary)")
            cur.execute("INSERT INTO salary (name, salary) values ('divu', 203574)")
            cur.execute("INSERT INTO salary (name, salary) values ('som', 103574)")
            cur.execute("select JSON_OBJECT('name', name) from salary")
            data=cur.fetchall()
            conn.commit()

            print(type(data))
            print(data)
            for d in data:
                print(d[0])
            a=json.dumps(data)
            #print(type(a))
            print(a)
        except Error as e:
            print(e)

        finally:
             conn.close()
        c=open('req.txt', 'rb')
        d=c.read()
        print(type(d))
        f=open('req1.txt', 'wb')
        f.write(d)

