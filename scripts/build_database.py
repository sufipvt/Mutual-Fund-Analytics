import sqlite3
# This creates the database file if it doesn't exist yet
connection = sqlite3.connect("data/db/mutual_fund.db")

# read the schema file
with open("sql/schema.sql","r") as f:
    schema_sql = f.read()

# Run all the CREATE TABLE statements in one go
connection.executescript(schema_sql)
connection.commit()

print("Database created with tables.")

cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

connection.close()