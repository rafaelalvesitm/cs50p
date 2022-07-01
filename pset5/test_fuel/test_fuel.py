import fuel, pytest

def main():
    test_convert()


def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/5") == 20
    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("1/0")
        assert fuel.convert("5/0")
    with pytest.raises(ValueError):
        assert fuel.convert("5/3")
        assert fuel.convert("10/5")
        assert fuel.convert("10.2/2.1")
        assert fuel.convert("10.2/2")
        assert fuel.convert("10/2.1")
        assert fuel.convert("10.2/2.1")


def test_gauce():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"


if __name__ == "__main__":
    main()