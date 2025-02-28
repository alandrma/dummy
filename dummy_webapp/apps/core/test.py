import sqlite3

def create_table():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

def authenticate(username, password):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)  # Debugging purpose
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials!")

if __name__ == "__main__":
    create_table()
    insert_user("admin", "password123")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate(username, password)
