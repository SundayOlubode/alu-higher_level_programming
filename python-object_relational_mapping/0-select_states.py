#!usr/bin/python3
""" 0-select_states.py """


import MySQLdb
import sys


def connect_db():
    """ Connect db with MySQLdb """
     db = MySQLdb.connect(
             host='localhost',
             port=3306
             user=sys.argv[1],
             passwd=sys.argv[2],
             db=sys.argv[3]
             )

     cur = db.cursor()

     cur.execute('SELECT * FROM states ORDERBY id')

     rows = cur.fetchall()

     for row in rows:
         print(row)

     cur.close()

     db.close()

if __name__ == "__main__":
    connect_db()
