import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.row_factory = sqlite3.Row

tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('Tables:', [t['name'] for t in tables])

# Check university count
try:
    count = conn.execute("SELECT COUNT(*) FROM universities_university").fetchone()[0]
    print('Universities:', count)
except:
    print('No universities table')

conn.close()