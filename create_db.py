# create_db.py
import sqlite3

# Connect to (or create) database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# -------------------------
# Create student table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# -------------------------
# Create feedback table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    text TEXT,
    sentiment TEXT,
    suggestion TEXT
)
""")
# -------------------------
# Insert 100 sample students
# -------------------------
students = []
for i in range(1, 101):
    reg_no = f"221CS{i:03d}"    # Example: 221CS001, 221CS002...
    password = f"pass{i:03d}"   # Example: pass001, pass002...
    students.append((reg_no, password))

cursor.executemany(
    "INSERT OR IGNORE INTO student (id, password) VALUES (?, ?)",
    students
)

# Commit and close connection
conn.commit()
conn.close()

print("Database created successfully with 100 students and feedback table!")