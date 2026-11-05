import os

# VULNERABILITY 1: Hardcoded AWS Credentials
# Bandit and the local scanner will flag this immediately
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

def get_user_data(username):
    # VULNERABILITY 2: SQL Injection
    # Taking direct user input and concatenating it into a query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def ping_server(ip_address):
    # VULNERABILITY 3: OS Command Injection
    # Allowing raw system commands to be executed
    os.system("ping -c 1 " + ip_address)