#!/usr/bin/python3
'''ists all cities from the database  hbtn_0e_0_usa'''

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
        SELECT c.id, c.name, s.name
        FROM cities as c
        INNER JOIN states as s
        ON c.state_id = s.id
        ORDER BY c.id ASC
        '''
    curr.execute(query)
    [print(city) for city in curr.fetchall()]
