import numb3rs

def test_ipv4_address():
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.512.512.512") == False
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("cat") == False
    assert numb3rs.validate("127.0.0.4000") == False
    assert numb3rs.validate("1000.2.3.4") == False
    assert numb3rs.validate("1.2000.3.4") == False
    assert numb3rs.validate("1.2.3000.4") == False
    assert numb3rs.validate("1.2.3.4000") == False
    assert numb3rs.validate("75.456.76.65") == False
    assert numb3rs.validate("valid.2.3.50") == False
    assert numb3rs.validate("1.valid.3.50") == False
    
    