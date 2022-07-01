import bank

def main():
    test_bank()


def test_twttr():
    assert bank.value("hello world") == 0
    assert bank.value("HELLO WORLD") == 0
    assert bank.value("hell yeah!") == 20
    assert bank.value("Home made") == 20
    assert bank.value("What is going on? ") == 100

if __name__ == "__main__":
    main()