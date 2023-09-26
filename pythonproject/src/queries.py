import sqlite3

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")

print(f"connection: {conn}")

# Step 2: Create a cursor object
cursor = conn.cursor()

# First query: Select all countries where social support is greater than the average social support
query_1 = "SELECT country FROM happiness_table WHERE social_support> (SELECT AVG(social_support) FROM happiness_table))"

for row in cursor.execute(query_1):
    print(row)

# Second query:
query_1 = "SELECT countries FROM happiness_table WHERE country LIKE 'A%'"

for row in cursor.execute(query_1):
    print(row)

conn.close()
