import sqlite3
from typing import List, Tuple, Union

class Database:
    def __init__(self, db_name: str = 'testeinternet.db'):
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()
        self.create_history_table()
        
    def create_history_table(self):
        """Create history table if it does not exist"""
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS history(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    data_hora TEXT,
                    ping TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    operadora TEXT NOT NULL,
                    upload TEXT NOT NULL,
                    download TEXT NOT NULL,
                    lon TEXT NOT NULL,
                    lat TEXT NOT NULL,
                    pais TEXT NOT NULL
                )
                """
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            
    def create_history(self, data_hora: str, ping: str, ip: str, operadora: str, 
                       upload: str, download: str, lon: str, lat: str, pais: str) -> Union[Tuple, None]:
        """Insert a new history record and return the created record"""
        try:
            self.cursor.execute(
                """
                INSERT INTO history(data_hora, ping, ip, operadora, upload, download, lon, lat, pais)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (data_hora, ping, ip, operadora, upload, download, lon, lat, pais)
            )
            self.con.commit()
            return self.cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 1").fetchone()
        except sqlite3.Error as e:
            print(f"Error inserting history record: {e}")
            return None
        
    def show_columns(self) -> List[str]:
        """Get list of column names in the history table"""
        try:
            self.cursor.execute("SELECT * FROM history LIMIT 1")
            col_name_list = [description[0] for description in self.cursor.description]
            print(f"Column names: {col_name_list}")
            return col_name_list
        except sqlite3.Error as e:
            print(f"Error fetching column names: {e}")
            return []
        
    def get_all_history(self) -> List[Tuple]:
        """Retrieve all history records"""
        try:
            get_history = self.cursor.execute("SELECT * FROM history").fetchall()
            #print(f"All history records: {get_history}")
            #print("get_history_type_db")
            #print(type(get_history))
            return get_history
        except sqlite3.Error as e:
            print(f"Error fetching history records: {e}")
            return []
        
    def close_db_connection(self):
        """Close the database connection"""
        try:
            if self.con:
                self.con.close()
                print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")
