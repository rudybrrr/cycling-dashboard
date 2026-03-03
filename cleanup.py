import sqlite3
conn = sqlite3.connect('rides.db')
conn.execute('DELETE FROM rides WHERE distance IS NULL OR distance = ""')
conn.commit()
conn.close()
print("Done")