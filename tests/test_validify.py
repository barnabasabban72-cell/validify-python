from validify import validate_email, validate_password, validate_phone, validate_url

def test_email():
    assert validate_email("student@gmail.com")
    assert not validate_email("studentgmail.com")

def test_password():
    assert validate_password("StrongPass1!")["valid"]
    assert not validate_password("1234")["valid"]

def test_phone():
    assert validate_phone("+233241234567")

def test_url():
    assert validate_url("https://github.com")
