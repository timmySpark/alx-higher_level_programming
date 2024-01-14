#!/usr/bin/python3
'''a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    curr = conn.cursor()
    query = '''
        SELECT * FROM cities as c
        INNER JOIN states as s
        ON c.state_id = s.id
        ORDER BY c.id
        '''
    curr.execute(query)
    print(", ".join(
                [city[2] for city in curr.fetchall() if city[4] == argv[4]]
                ))
