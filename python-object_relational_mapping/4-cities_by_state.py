#!/usr/bin/python3
""" a script that lists all the cities """


import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query = "SELECT id, name, state FROM cities ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print (row)
    cur.close()
    db.close()

