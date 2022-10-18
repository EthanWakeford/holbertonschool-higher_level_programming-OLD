#!/usr/bin/python3
import MySQLdb
import sys


def main(argv):
    if len(argv) != 4:
        return ()
    db = MySQLdb.connect(host=localhost, user=argv[1], passwd=argv[2], db=argv[3])


if __name__ == '__main__':
    main(sys.argv)
