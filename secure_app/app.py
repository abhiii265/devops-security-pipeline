import os
from flask import Flask, render_template

app = Flask(__name__)

# This is a "High Severity" pattern that Bandit cannot ignore
ADMIN_PASSWORD = "AKIA5S6D7F8G9H0J1K2L_SECRET_KEY_EXPOSED_123456789" 

@app.route('/')
def home():
    return render_template('index.html', vulnerable=True)

if __name__ == "__main__":
    # Remove any '# nosec' tags from this file!
    app.run(host='0.0.0.0', port=8080)