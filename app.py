from db_manager import load_csv_to_db, run_sql_query
from llm_utils import generate_sql_with_explanation

print("AI Spreadsheet Assistant (LLM + Explanation)")
print("Type commands like:")
print("- load example.csv")
print("- show me top revenue this month")
print("- exit")

def get_schema_description():
    import sqlite3
    conn = sqlite3.connect("assistant.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    schema = ""
    for (table_name,) in tables:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        schema += f"- {table_name} ({', '.join(column_names)})\n"

    conn.close()
    return schema if schema else "No tables loaded."

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        print("Goodbye.")
        break

    elif user_input.startswith("load "):
        csv_path = user_input.split("load ")[1]
        load_csv_to_db(csv_path)

    else:
        schema_info = get_schema_description()
        output = generate_sql_with_explanation(user_input, schema_info)

        # Separate SQL and explanation
        if "-- SQL Query:" in output and "-- Explanation:" in output:
            sql_section = output.split("-- SQL Query:")[1].split("-- Explanation:")[0].strip()
            explanation = output.split("-- Explanation:")[1].strip()
        else:
            sql_section = output
            explanation = "(No explanation found)"

        print(f"\n[Generated SQL]:\n{sql_section}")
        print(f"\n[Explanation]:\n{explanation}\n")
        result = run_sql_query(sql_section)
        print(result)
