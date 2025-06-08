import sqlite3

conn = sqlite3.connect('posts.db') 
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    body TEXT
)
''')

posts = [
    ('文章1', '文章1的內容。'),
    ('文章2', '文章2的內容。'),
    ('文章3', '文章3的內容。')
]

cursor.executemany('''
INSERT INTO posts (title, body)
VALUES (?, ?)
''', posts)

conn.commit()

cursor.execute('SELECT * FROM posts')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
