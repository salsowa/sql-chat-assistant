import openai
import os

# Set your API key here (recommended to use environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Optionally, hardcode your key directly for testing (not recommended for public repos)
# openai.api_key = "sk-..."

def generate_sql(user_input, schema):
    prompt = f"""
You are a helpful assistant that converts natural language questions into SQL queries.
Here is the table schema:
{schema}

User question: {user_input}
SQL query:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100,
    )
    return response["choices"][0]["message"]["content"].strip()
