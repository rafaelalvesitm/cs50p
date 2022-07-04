import working, pytest

def main():
    test_valid_format()
    test_invalid_format()
    test_invalid_hour()
    test_invalid_minute()

def test_valid_format():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert working.convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        working.convert("9 AM - 5 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        working.convert("13:00 AM to 16:00 PM")

def test_invalid_minute():
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:60 PM")
