import re

def validate_password(password):
    issues = []
    if not isinstance(password, str):
        return {"valid": False, "issues": ["Password must be text."]}
    if len(password) < 8:
        issues.append("Use at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        issues.append("Add an uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Add a lowercase letter.")
    if not re.search(r"\d", password):
        issues.append("Add a number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Add a special character.")
    return {"valid": not issues, "issues": issues}
