#!/usr/bin/python3

"""
This script retrieves and prints all states from the database hbtn_0e_0_usa
that begin with the letter 'N'.

Usage: ./script_name.py <db_username> <db_password> <db_name>
"""

import sys
import MySQLdb


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("""
        SELECT * FROM states
        WHERE name LIKE 'N%' COLLATE utf8_bin
        ORDER BY id ASC
    """)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
