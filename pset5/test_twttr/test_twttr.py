import twttr

def main():
    test_twttr()


def test_twttr():
    assert twttr.shorten("hello world") == "hll wrld"
    assert twttr.shorten("HELLO WORLD") == "HLL WRLD"
    assert twttr.shorten("Twitter!") == "Twttr!"
    assert twttr.shorten("RAFAEL_10") == "RFL_10"
    assert twttr.shorten("rafael1") == "rfl1"

if __name__ == "__main__":
    main()