#!/usr/bin/python3
'''
    script that lists all states lists all states with a name starting with N
'''

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sta_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` LIKE %s ORDER BY `id` ASC"
    cursor.execute(query, (sta_name, ))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
