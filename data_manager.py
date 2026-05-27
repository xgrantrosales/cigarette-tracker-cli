import sqlite3

# Opens connection to the SQLite database file.
def connect_database():
    connection = sqlite3.connect("cigarette_tracker.db")
    return connection

# Creates the records table if it does not exist yet.
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, daily_limit INTEGER, smoked INTEGER, remaining INTEGER, status TEXT)")
    connection.commit()
    connection.close()

# Inserts one new record into the database.
def insert_record(date, daily_limit, smoked, remaining, status):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO records(date, daily_limit, smoked, remaining, status) VALUES(?,?,?,?,?)", (date, daily_limit, smoked, remaining, status))
    connection.commit()
    connection.close()

# Fetches all records from the database.
def fetch_records():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    connection.close()
    return records

# Updates an existing record using its ID.
def update_record(record_id, new_daily_limit, new_smoked, new_remaining, new_status):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("UPDATE records SET daily_limit = ? , smoked = ? , remaining = ? , status = ? WHERE id = ?", (new_daily_limit, new_smoked, new_remaining, new_status, record_id))
    connection.commit()
    connection.close()

# Deletes a record using its ID.
def delete_record(record_id):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))    
    connection.commit()
    connection.close()




    