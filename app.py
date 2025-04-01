from db_manager import load_csv_to_db, run_sql_query
from llm_utils import generate_sql

print("AI Spreadsheet Assistant")
print("Type commands like:")
print("- load example.csv")
print("- Ask any question about the data")
print("- exit")

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        print("Goodbye.")
        break

    elif user_input.startswith("load "):
        csv_path = user_input.split("load ")[1]
        load_csv_to_db(csv_path)

    else:
        schema = "id, name, region, revenue"
        sql = generate_sql(user_input, schema)
        print(f"[Generated SQL]: {sql}")
        result = run_sql_query(sql)
        print(result)
