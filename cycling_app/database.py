import sqlite3

def init_db(): 
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rides (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   distance REAL, 
                   duration INTEGER, 
                   date TEXT
                )
    ''')
    conn.commit()
    conn.close()

def insert_ride(distance, duration, date): 
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rides (distance, duration, date) VALUES (?, ?, ?)", (distance, duration, date))
    conn.commit()
    conn.close()

def get_rides(): 
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rides")
    rides = cursor.fetchall()
    conn.commit()
    conn.close()
    return rides

def get_stats(): 
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(distance) AS total_distance, SUM(duration) AS total_duration FROM rides")
    stats = cursor.fetchone()
    conn.commit()
    conn.close()
    return stats