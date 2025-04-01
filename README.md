# sql-chat-assistant
Chat-based spreadsheet assistant that loads CSV files and answers questions using SQL queries.
# SQL Chat Assistant
This is a chat-based spreadsheet assistant developed for a hackathon project.
## Features
- Load a CSV file as a database table
- Ask natural-language questions like:
  - "Show me top revenue"
  - "Show me north region"
- Mock LLM logic generates SQL queries from user prompts
- Results are displayed in the console
- Powered by Python, SQLite, and Pandas

**How to Run This Project**
1. Clone the repo
git clone https://github.com/your-username/sql-chat-assistant
cd sql-chat-assistant
2. Install the requirements
pip install -r requirements.txt
3. Run the assistant
python app.py
4. Inside the assistant, type:
load example.csv
show me top revenue
exit
**You will see the following table based on example.csv:**
id,name,region,revenue
1,Alice,North,12000
2,Bob,East,9000
3,Charlie,South,15000
4,Diana,West,7000
5,Evan,North,13000
Expected output:

[Generated SQL]: SELECT name, revenue FROM data ORDER BY revenue DESC LIMIT 3
      name  revenue
0  Charlie    15000
1     Evan    13000
2    Alice    12000
