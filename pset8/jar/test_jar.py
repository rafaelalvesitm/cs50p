from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(capacity=10)
    assert jar.capacity == 10
    assert jar.size == 0

    jar = Jar(capacity=10, size=5)
    assert jar.capacity == 10
    assert jar.size == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(11)
    assert jar.size == 0
