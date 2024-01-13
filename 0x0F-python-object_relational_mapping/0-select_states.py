#!/usr/bin/python3
# List all the sataes from database hbtn_0e_0_usa
#  Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    curr = conn.cursor()
    curr.execute("select * FROM states")
    [print(state) for state in curr.fetchall()]
    curr.close()
    conn.close()
