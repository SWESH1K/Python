import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()


# exexute will work but will throw an error if this file runned second time.
# cur.execute('''CREATE TABLE TODO (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         priority INTEGER NOT NULL
# );''')


# This is a better way
cur.execute('''CREATE TABLE IF NOT EXISTS TODO (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
);''')

# This is used to insert only one data
# cur.execute('''INSERT INTO TODO (name,priority) VALUES (?,?)''',('My first task',1))

# Here is a method to execute many data in a single time.

tasks = [
    ('My Second Task',5),
    ('My Third Task',10),
    ('My Fourth Task',15)
]
cur.executemany("INSERT INTO TODO(name, priority) VALUES (?,?)", tasks)

conn.commit()
conn.close()