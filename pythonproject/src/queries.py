"""
This module contains queries for the happiness database.
"""

import sqlite3

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# First query: Select all countries where social support is greater than the average social support
QUERY_1 = "SELECT country FROM happiness_table WHERE social_support > \
(SELECT AVG(social_support) FROM happiness_table)"

for i in cursor.execute(QUERY_1):
    print(i)

# Second query:
QUERY_2 = "SELECT country FROM happiness_table WHERE country LIKE 'A%'"

for i in cursor.execute(QUERY_2):
    print(i)

conn.close()
