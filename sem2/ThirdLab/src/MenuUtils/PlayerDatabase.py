import sqlite3

class PlayerDatabase:

    def __init__(self):
        self.db_name = 'MenuUtils/database/players.db'
        self._create_table()

    def _create_table(self):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            create_table_query = """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")
        finally:
            if connection:
                connection.close()

    def add_player(self, name: str, score: int):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            insert_query = "INSERT INTO players (name, score) VALUES (?, ?);"
            cursor.execute(insert_query, (name, score))
            connection.commit()

        except sqlite3.Error as e:
            print(f"Ошибка при добавлении игрока: {e}")
        finally:
            if connection:
                connection.close()

    def get_all_players(self):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            select_query = "SELECT name, score FROM players;"
            cursor.execute(select_query)
            players = cursor.fetchall()

            return players
        except sqlite3.Error as e:
            print(f"Ошибка при получении данных: {e}")
            return []
        finally:
            if connection:
                connection.close()
                print("Соединение с базой данных закрыто.")