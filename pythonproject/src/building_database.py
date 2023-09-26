"""
This module creates a SQLite database from a CSV file.
"""

import sqlite3
import csv

# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Drop the table if it exists
DROP_TABLE_SQL = "DROP TABLE IF EXISTS happiness_table"
cursor.execute(DROP_TABLE_SQL)

# Step 4: Create a table with the desired schema
CREATE_TABLE_SQL = """
CREATE TABLE happiness_table (
    country TEXT PRIMARY KEY,
    log_gdp_pc FLOAT,
    social_support FLOAT,
    life_exp FLOAT,
    freedom FLOAT,
    generosity FLOAT,
    corruption FLOAT
)
"""
cursor.execute(CREATE_TABLE_SQL)

# Step 5: Open the CSV file and populate the SQLite table
CSV_FILE_PATH = "pythonproject/src/data/happiness_data.csv"

with open(CSV_FILE_PATH, "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        cursor.execute(
            "INSERT INTO happiness_table(country, \
            log_gdp_pc, social_support, life_exp, \
            freedom, generosity, corruption) VALUES (?, ?, ?, ?, ?, ?, ?)",
            row,
        )

# Step 6: Commit the changes and close the connection
conn.commit()
conn.close()
