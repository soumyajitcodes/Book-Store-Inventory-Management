import sqlite3

def connect():
    """
    This function:
    1. Creates a connection
    2. Creates a cursor object
    3. Creates a table if not exists
    4. Commit the changes
    5. Close the connection
    """
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookTable(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

# Add Entry to database
def addEntry(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO bookTable values (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()

# View all data from database
def viewAll():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM bookTable")
    rows = cur.fetchall()
    connection.close()
    return rows

# Search Entries
def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM bookTable WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    connection.close()
    return rows

# Delete Records
def deleteRecords(id):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM bookTable WHERE id=?", (id,))
    connection.commit()
    connection.close()

#  Update Entry
def updateEntry(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("UPDATE bookTable SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    connect()