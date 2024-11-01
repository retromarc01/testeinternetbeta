import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
        self.fetch_data()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )''')
        self.connection.commit()

    def insert_data(self, data):
        self.cursor.execute('INSERT INTO my_table (data) VALUES (?)', (data,))
        self.connection.commit()

    def fetch_data(self):
        teste = self.cursor.execute('SELECT * FROM my_table') #('SELECT * FROM my_table')
        print(str(teste.fetchall))
        return self.cursor.fetchall()
    
    def show_table(self):
        self.cursor.execute("SELECT * FROM my_table")
        col_name_list = [tuple[0] for tuple in self.cursor.description]
        print(col_name_list)
        return col_name_list

    def close(self):
        self.connection.close()
