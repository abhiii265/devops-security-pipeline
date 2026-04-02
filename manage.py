# ==========================================
# DANGER: VULNERABLE CODE FOR TESTING ONLY
# ==========================================
import os
import hashlib

def insecure_testing_functions(user_input):
    # Vulnerability 1: Hardcoded Secret/Password
    aws_secret_key = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY"
    
    # Vulnerability 2: Shell/Command Injection
    # (Allowing random user input to run as a system command)
    os.system("ping " + user_input)
    
    # Vulnerability 3: Using a broken, outdated encryption method (MD5)
    weak_hash = hashlib.md5(b"password123").hexdigest()
    
    return aws_secret_key, weak_hash