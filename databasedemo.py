import sqlite3

conn = sqlite3.connect("gastrotour.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
               name text,
               last_name text,
               date_of_birth text
)
""")

conn.commit()
conn.close()