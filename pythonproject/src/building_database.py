import sqlite3
import csv
import os


# Step 1: Establish a connection to the SQLite database
conn = sqlite3.connect("pythonproject/src/data/happiness_database.db")


# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table with the desired schema
create_table_sql = """
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
cursor.execute(create_table_sql)

# Step 4: Open the CSV file and populate the SQLite table

csv_file_path = "pythonproject/src/data/happiness_data.csv"

with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        # Assuming your CSV has columns: id, name, age, city
        cursor.execute(
            "INSERT INTO happiness_table(country, log_gdp_pc, social_support, life_exp, freedom, generosity, corruption) VALUES (?, ?, ?, ?, ?, ?, ?)",
            row,
        )

# Step 5: Commit the changes and close the connection
conn.commit()
conn.close()
