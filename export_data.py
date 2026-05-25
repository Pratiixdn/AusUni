import sqlite3
import json

conn = sqlite3.connect('db.sqlite3')
conn.row_factory = sqlite3.Row

tables = [
    'universities_state',
    'universities_city', 
    'universities_university',
    'universities_campus',
    'universities_course',
    'universities_course_campus',
    'universities_scholarship',
    'blog_blogpost',
]

all_data = {}
for table in tables:
    rows = conn.execute(f"SELECT * FROM {table}").fetchall()
    all_data[table] = [dict(row) for row in rows]
    print(f"{table}: {len(rows)} rows")

with open('data_export.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=True, indent=2)

print('Done! Saved to data_export.json')
conn.close()