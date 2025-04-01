import pandas as pd
import sqlite3
import os

def load_csv_to_db(csv_path, db_name="assistant.db", table_name="data"):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Loaded {csv_path} into table '{table_name}'")

def run_sql_query(query, db_name="assistant.db"):
    conn = sqlite3.connect(db_name)
    try:
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result
    except Exception as e:
        conn.close()
        return f"Error: {e}"
