import sqlite3

try:
    connection = sqlite3.connect("simple_sql.db", timeout=5)
    print("[*] Connect with database 'simple_sql.db'")

    cursor = connection.cursor()
    print("[*] Create cursor database 'simple_sql.db'")

    # sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
    #                             id INTEGER PRIMARY KEY,
    #                             name TEXT NOT NULL,
    #                             email text NOT NULL UNIQUE,
    #                             joining_date datetime,
    #                             salary REAL NOT NULL);'''
    #
    # cursor.execute(sqlite_create_table_query)
    # print("[*] Create table 'sqlitedb_developers' in database 'simple_sql.db'")

    with open("sqlite_create_tables.sql", "r") as file_database:
        cursor.executescript(file_database.read())
    print("[*] Create table 'sqlitedb_developers' in database 'simple_sql.db' from file 'sqlite_create_tables.sql'")

    cursor.execute(
        """INSERT INTO fruits VALUES
        (1, 'fruits_1', 100),
        (2, 'fruits_2', 200);""")
    print("[*] Added data in table 'fruits' in database 'simple_sql.db'")

    connection.commit()
    cursor.close()
    print("[*] Commit in database 'simple_sql.db' and close cursor")

except sqlite3.Error as error:
    print(f"Error: {error}")
finally:
    if connection:
        print(f"[*] Changed rows in the database 'simple_sql.db': {connection.total_changes}")
        connection.close()
        print("[*] Close connect with database 'simple_sql.db'")
