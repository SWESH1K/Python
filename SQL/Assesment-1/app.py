import sqlite3

class DATA:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("sql_database.db")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute('''CREATE TABLE IF NOT EXISTS DATA(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
        );''')

    def add_task(self):
        name = input("Please enter the name of task: ")
        priority = int(input("Please enter the priority of task: "))

        self.curr.execute("INSERT INTO DATA (name,priority) VALUES (?,?)", (name,priority))
        self.conn.commit()

    def show_tasks(self):
        print("The rows in the table are: ".center(40,"-"))
        for row in self.curr.execute("SELECT * FROM DATA"):
            print(row)

    def change_priority(self,id):
        if(id<1):
            print("Please enter a valid id");return
        priority = int(input("Please enter the new priority: "))
        self.curr.execute("UPDATE DATA SET priority=? WHERE id=?",(priority,id))
        self.conn.commit()

    def delete_task(self,id):
        self.curr.execute("DELETE FROM DATA WHERE id=?",(id,))
        print("Data deleted at id =",id)
        self.conn.commit()

def main():
    print("Welcome to mySQL".center(40,'-'))
    mysql = DATA()
    while(1):
        options = ["\n1,Show tasks","2,Add Task","3,Change Priority","4,Delete Task","5,Exit"]
        for x in options: print(x)
        inp = int(input("Please select one of the options from above: "))
        match inp:
            case 1:
                mysql.show_tasks()
            case 2:
                mysql.add_task()
            case 3:
                id = int(input("Please enter the id: "))
                mysql.change_priority(id)
            case 4:
                id = int(input("Please enter the id: "))
                mysql.delete_task(id)
            case 5:
                print("Exited!")
                exit()
            case _:
                print("Please enter a valid number!")

if __name__ == '__main__':
    main()