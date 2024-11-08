import sqlite3

def setup_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        professor_id INTEGER,
        FOREIGN KEY (professor_id) REFERENCES professors (id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS time_slots (
        id INTEGER PRIMARY KEY,
        day TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL
    )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()

# Run the setup
setup_database()
