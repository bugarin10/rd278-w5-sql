import sqlite3

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("data/happiness_database.db")

# print(f"connection: {conn}")

# Step 2: Create a cursor object
cursor = conn.cursor()

# First query: Select all countries where social support is greater than the average social support
query_1 = "SELECT country FROM happiness_table WHERE social_support > (SELECT AVG(social_support) FROM happiness_table)"

for i in cursor.execute(query_1):
    print(i)

# Second query:
query_2 = "SELECT country FROM happiness_table WHERE country LIKE 'A%'"

for i in cursor.execute(query_2):
    print(i)

conn.close()
