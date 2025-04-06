import openai
import os

def generate_sql_with_explanation(user_input, schema_description):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
You are an AI assistant tasked with converting user queries into SQL statements.
The database uses SQLite and contains the following schema:

{schema_description}

User Query:
"{user_input}"

Your task is to:
1. Generate a SQL query that accurately answers the user's question.
2. Ensure the SQL is compatible with SQLite syntax.
3. Provide a short comment explaining what the query does.

Output Format:
-- SQL Query:
<your query>

-- Explanation:
<your explanation>
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response['choices'][0]['message']['content'].strip()
