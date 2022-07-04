import um


def test_um():
    assert um.count("um") == 1
    assert um.count("um um") == 2
    assert um.count("um...") == 1
    assert um.count("um?") == 1
    assert um.count("...um") == 1
    assert um.count("instrumentation cryptosporidium") == 0
    assert um.count("Um") == 1
    assert um.count("UM") == 1
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um, thanks, um...") == 2
