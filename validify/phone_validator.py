import re

def validate_phone(phone):
    if not isinstance(phone, str):
        return False
    cleaned = phone.replace(" ", "").replace("-", "")
    return bool(re.match(r"^\+?\d{10,15}$", cleaned))
