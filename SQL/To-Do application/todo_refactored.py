import sqlite3

class TODO:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.curr = self.conn.cursor()
        self.create_table_task()

    def create_table_task(self):
        self.curr.execute('''CREATE TABLE IF NOT EXISTS TODO(
                          id INTEGER PRIMARY KEY,
                          name TEXT NOT NULL,
                          priority INTEGER NOT NULL
        );''')
    
    def add_values(self,name,priority):
        self.curr.execute("INSERT INTO TODO (name, priority) VALUES (?,?)",(name,priority))
        self.conn.commit()

    def print_database(self):
        # for row in self.curr.execute("SELECT * FROM TODO"):
        #     print(row)
        # or
        self.curr.execute('SELECT * FROM TODO')
        rows = self.curr.fetchall()
        for row in rows:
            print(row)

def main():
    app = TODO()
    # app.add_values('My Fourth Task',20)
    app.print_database()

if __name__ == '__main__':
    main()