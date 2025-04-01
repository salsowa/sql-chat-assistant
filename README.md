# sql-chat-assistant
Chat-based spreadsheet assistant that loads CSV files and answers questions using SQL queries.
# SQL Chat Assistant
This is a chat-based spreadsheet assistant developed for the  hackathon project.
 Load a CSV file into a SQLite database
- Ask natural-language questions like:
  - "Show me top revenue"
  - "Who is in the North region?"
  - "What is the total revenue?"
- GPT-3.5 (via OpenAI API) converts chat into SQL
- Results shown directly in the terminal

**How to Run This Project**
1. Clone the Repo
git clone https://github.com/YOUR_USERNAME/sql-chat-assistant
cd sql-chat-assistant
2. Install Requirements
pip install -r requirements.txt
3. Set Your OpenAI API Key
In PowerShell:
$env:OPENAI_API_KEY="sk-your-secret-key"
4. Start the App
python app.py
5. Inside the Assistant:
> load example.csv
> show me the top 3 revenue
> who is from the North region?
> what is the total revenue?
>
> example from powershell terminal 
> - show me top revenue
- exit
> who is in the North region?
[Generated SQL]: SELECT * FROM data WHERE region = 'North'
   id   name region  revenue
0   1  Alice  North    12000
1   5   Evan  North    13000
> what is the total revenue?
[Generated SQL]: SELECT * FROM data LIMIT 5
   id     name region  revenue
0   1    Alice  North    12000
1   2      Bob   East     9000
2   3  Charlie  South    15000
3   4    Diana   West     7000
4   5     Evan  North    13000
>
