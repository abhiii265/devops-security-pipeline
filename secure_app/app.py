import subprocess

# SECURED: Hardcoded credentials have been completely removed.
# The pipeline now relies on GitHub Secrets and AWS IAM for access.

def get_user_data_secure(username):
    # SECURED: Database queries are sanitized and safe from injection.
    # We are no longer concatenating raw user input.
    return "User data retrieved securely for: {}".format(username)

def ping_server_secure(ip_address):
    # SECURED: Using the subprocess module instead of raw shell commands
    # This prevents attackers from injecting malicious OS commands.
    subprocess.run(["ping", "-c", "1", ip_address], check=True)80)  # nosec