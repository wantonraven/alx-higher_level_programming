#!/usr/bin/python3
"""
 a script that lists all states with a name starting \
         with N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Get data from database
    """

    db_conct = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = db_conct.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(argv[4]))

    states_name = cursor.fetchall()

    for state in states_name:
        print(state)

    cursor.close()
    db_conct.close()
