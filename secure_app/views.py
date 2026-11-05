from django.shortcuts import render
from django.conf import settings

def dashboard_view(request):
    # This points directly to your app.py file
    app_file_path = settings.BASE_DIR / 'secure_app' / 'app.py'
    
    is_secure = True
    vulnerabilities = []
    
    try:
        with open(app_file_path, 'r') as file:
            code = file.read()
            
            # SCANNER RULE 1: SQL Injection
            if "SELECT * FROM" in code and "+" in code:
                is_secure = False
                vulnerabilities.append({
                    "type": "SQL Injection",
                    "severity": "HIGH",
                    "desc": "Direct user input is being concatenated into a database query without sanitization."
                })
                
            # SCANNER RULE 2: OS Command Injection
            if "os.system" in code:
                is_secure = False
                vulnerabilities.append({
                    "type": "OS Command Injection",
                    "severity": "CRITICAL",
                    "desc": "Application is passing unsanitized input directly to the system shell."
                })
                
            # SCANNER RULE 3: Hardcoded Secrets
            if "AWS_ACCESS_KEY_ID" in code or "AKIA" in code:
                is_secure = False
                vulnerabilities.append({
                    "type": "Hardcoded Credentials",
                    "severity": "CRITICAL",
                    "desc": "The scanner detected exposed AWS access keys in the source code."
                })
    except FileNotFoundError:
        pass

    # Send the scan results to the HTML page
    return render(request, 'index.html', {
        'is_secure': is_secure,
        'vulnerabilities': vulnerabilities
    })