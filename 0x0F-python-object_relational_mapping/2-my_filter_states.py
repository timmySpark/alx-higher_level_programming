#!/usr/bin/python3
'''takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument'''

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
        SELECT * FROM states
        WHERE name='{}'
        ORDER BY id ASC
        '''.format(argv[4])
    curr.execute(query)
    [print(state) for state in curr.fetchall()]
    curr.close()
    conn.close()
