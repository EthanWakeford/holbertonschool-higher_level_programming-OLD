#!/usr/bin/python3
"""print all states from database where name matches the argument safely."""
import MySQLdb
import sys


def main(argv):
    """Guards content."""
    if len(argv) != 5:
        return ()
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id = \
        (SELECT id from states where name = %(name)s)\
            ORDER BY cities.id", {'name': argv[4]})
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row[0])
    print(", ".join(my_list))
    cur.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
