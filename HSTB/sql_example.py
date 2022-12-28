import sqlite3
import os

# Make a database and a table (download sqlite db browser to look inside the file)
try:
    os.remove(r"c:\temp\test.db")
except FileNotFoundError:
    pass
conn = sqlite3.connect(r"c:\temp\test.db")
cur = conn.cursor()
cur.execute("CREATE TABLE players (name text, age integer, gpa real)")

# Add a couple records
cur.execute("insert into players values(?, ?, ?)", ["connor", 18, 3.5])
cur.execute("insert into players values(?, ?, ?)", ["mikey", 17, 3.3])

# retrieve the records
print(cur.execute("SELECT * FROM players").fetchall())

# Edit a field of a record
cur.execute("update players set (gpa)=(?)", [3.5])

# See if the edit worked
print(cur.execute("SELECT * FROM players").fetchall())
print(cur.execute("SELECT * FROM players WHERE name=(?)", ["connor"]).fetchall())

# get things back like a dictionary (accessible by column name)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
data = cur.execute("SELECT * FROM players WHERE name=(?)", ["connor"]).fetchone()
print(data['name'], data['gpa'])
conn.close()


