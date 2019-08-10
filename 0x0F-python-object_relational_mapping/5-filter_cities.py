#!/usr/bin/python3
"""5-filter_cities
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT cities.name\
                    FROM cities\
                    LEFT JOIN states\
                    ON cities.state_id=states.id\
                    WHERE states.name = %s\
                    ORDER by cities.id ASC", (argv[4],))
        table = db.fetchall()
        print(", ".join([data[0] for data in table]))
