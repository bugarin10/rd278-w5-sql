"""
This module contains queries for the happiness database.
"""
import sqlite3
import fire

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# First query: Select all countries where social support is greater than the average social support
QUERY_1 = "SELECT * FROM happiness_table WHERE social_support > \
(SELECT AVG(social_support) FROM happiness_table) LIMIT 3"

for c in cursor.execute(QUERY_1):
    print(c)

print("\n")

# Second query:
QUERY_2 = "SELECT country FROM happiness_table WHERE country LIKE 'A%'"

for i in cursor.execute(QUERY_2):
    print(i)

print("\n")

conn.close()


def main(query):
    """
    Main function for the queries module.
    """
    # Step 1: Establish a connection to the SQLite database
    conn2 = sqlite3.connect("pythonproject/src/data/happiness_database.db")

    # Step 2: Create a cursor object
    cursor2 = conn2.cursor()

    # First query: Select all countries where social
    # support is greater than the average social support
    query_1 = query

    for k in cursor2.execute(query_1):
        print(k)
    print("\n")

    conn2.close()


if __name__ == "__main__":
    fire.Fire(main)
