def validate_username(username, min_length=3, max_length=20):
    if not isinstance(username, str):
        return False
    if not (min_length <= len(username) <= max_length):
        return False
    return username.replace("_", "").isalnum()

def validate_required_field(value):
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True

def validate_numeric_range(value, minimum, maximum):
    if not isinstance(value, (int, float)):
        return False
    return minimum <= value <= maximum
