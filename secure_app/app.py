import sqlite3
import os

# FLAG 1: Hardcoded Secrets (Scanners like TruffleHog or GitLeaks will catch this)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "super_secret_admin_password_123!"

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # FLAG 2: SQL Injection (Scanners like Bandit or SonarQube will catch this)
    # Taking direct user input and putting it into a database query is highly dangerous
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    return cursor.fetchall()

def ping_server(ip_address):
    # FLAG 3: OS Command Injection
    # A hacker could pass an IP address like "8.8.8.8; rm -rf /" to delete the server
    os.system("ping -c 1 " + ip_address)

print("App is running...")