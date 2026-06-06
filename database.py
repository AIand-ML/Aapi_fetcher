import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("weather.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            windspeed REAL,
            search_time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def save_weather(self, city, temp, wind):

        self.cursor.execute("""
        INSERT INTO weather_history
        (city, temperature, windspeed)
        VALUES (?, ?, ?)
        """, (city, temp, wind))

        self.conn.commit()

    def get_history(self):

        self.cursor.execute("""
        SELECT city,
               temperature,
               windspeed,
               search_time
        FROM weather_history
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()