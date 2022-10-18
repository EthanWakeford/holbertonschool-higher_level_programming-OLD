#!/usr/bin/python3
import MySQLdb
import sys


def main(argv):
    if len(argv) != 4:
        return ()
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states")
    print(states)
    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
