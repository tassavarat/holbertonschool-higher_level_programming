#!/usr/bin/python3
"""4-cities_by_state
Lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id=states.id\
                    ORDER by cities.id ASC")
        table = db.fetchall()
        for data in table:
            print(data)
