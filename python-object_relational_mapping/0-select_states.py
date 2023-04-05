#!/usr/bin/python3
import sys
import MySQLdb

# Get the database connection details from command-line arguments
user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=password, db=db_name)

# Create a cursor object
cur = db.cursor()

# Execute a SELECT statement to retrieve all the rows from the `states` table
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows
rows = cur.fetchall()

# Print the rows in the desired format
for row in rows:
    print(row)

# Close the cursor and database connection
cur.close()
db.close()
