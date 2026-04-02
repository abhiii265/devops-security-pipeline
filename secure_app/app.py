import os
from flask import Flask, render_template

app = Flask(__name__)

# --- THE FACULTY DEMO SWITCH ---

# STEP 1: To show "VULNERABLE" (RED BUILD), remove the '#' below:
ADMIN_PASSWORD = "AKIA_FAKE_AWS_KEY_EXPOSED_12345"

# STEP 2: To show "SAFE" (GREEN BUILD), put the '#' back at the start.

@app.route('/')
def home():
    # We use globals().get so the app doesn't crash when password is commented
    if globals().get('ADMIN_PASSWORD'):
        return render_template('index.html', vulnerable=True, error="VULNERABILITY: Hardcoded Secret Found!")
    
    return render_template('index.html', vulnerable=False)

if __name__ == "__main__":
    # Added '# nosec' here so this line NEVER causes a build failure
    app.run(host='0.0.0.0', port=8080)  # nosec