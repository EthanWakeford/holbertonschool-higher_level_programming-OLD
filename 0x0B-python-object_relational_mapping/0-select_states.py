#!/usr/bin/python3
"""uses mysqldb to print all states from database"""
import MySQLdb
import sys


def main(argv):
    """main function to guard content"""
    if len(argv) != 4:
        return ()
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
