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
    query = "SELECT  cities.name FROM cities LEFT JOIN states\
                ON cities.state_id = states.id WHERE states.name = %s\
                ORDER BY cities.id"
    cursor.execute(query, (sta_name, ))
    results = cursor.fetchall()
    tmp = []
    for row in results:
        tmp.append(row[0])
    print(*tmp, sep=", ")
    cursor.close()
    db.close()
