import plates


def main():
    test_alphanumeric()
    test_lenght()
    test_numbers()
    test_zero()


def test_alphanumeric():
    assert plates.is_valid("222AAA") == False
    assert plates.is_valid("AAABBB") == True
    assert plates.is_valid("AAAB!!") == False
    assert plates.is_valid("!!ABBB") == False
    assert plates.is_valid(" AAABBB") == False
    assert plates.is_valid(".AAAABN") == False
    assert plates.is_valid("AAAABN ") == False
    assert plates.is_valid("10AABN") == False
    assert plates.is_valid("CS") == True
    assert plates.is_valid("11") == False


def test_lenght():
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA222AAA") == False
    assert plates.is_valid("A") == False


def test_numbers():
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AA222A") == False


def test_zero():
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA022") == False


if __name__ == "__main__":
    main()
