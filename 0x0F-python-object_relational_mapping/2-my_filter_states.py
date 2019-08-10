#!/usr/bin/python3
"""2-my_filter_states.py module
Takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT *\
                   FROM states\
                   WHERE name\
                   LIKE BINARY '{}'\
                   ORDER BY id ASC".format(argv[4]))
        table = db.fetchall()
        for data in table:
            print(data)
