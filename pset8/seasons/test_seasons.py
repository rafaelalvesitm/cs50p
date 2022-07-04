import seasons, pytest

from datetime import date

def test_valid_date():
    assert seasons.validate_date("1999-01-01") == date(1999, 1, 1)
    assert seasons.validate_date("1998-01-01") == date(1998, 1, 1)
    assert seasons.validate_date("1998-06-01") == date(1998, 6, 1)
    assert seasons.validate_date("1998-06-20") == date(1998, 6, 20)

def test_invalid_date():
    with pytest.raises(SystemExit):
        assert seasons.validate_date("1999-13-01")
        assert seasons.validate_date("1999-01-32")
        assert seasons.validate_date("February 6th, 1998")
