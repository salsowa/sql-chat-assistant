def mock_generate_sql(user_input):
    if "top revenue" in user_input.lower():
        return "SELECT name, revenue FROM data ORDER BY revenue DESC LIMIT 3"
    elif "north region" in user_input.lower():
        return "SELECT * FROM data WHERE region = 'North'"
    else:
        return "SELECT * FROM data LIMIT 5"
