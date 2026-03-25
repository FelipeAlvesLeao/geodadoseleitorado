import sqlite3
import pandas as pd
import os

class DatabaseManager:
    def __init__(self, db_path="data/processed/eleitorado.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def save_dataframe(self, df, table_name="perfil_eleitorado"):
        with self.get_connection() as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)

    def execute_query(self, query):
        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn)