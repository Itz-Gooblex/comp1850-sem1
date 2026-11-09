from weather import comfort_level

def test_cold():
    assert comfort_level(10) == "COLD"
    assert comfort_level(15) == "COLD"

def test_ok():
    assert comfort_level(15) == "OK"
    assert comfort_level(18) == "OK"
    assert comfort_level(25) == "OK"

def test_hot():
    assert comfort_level(25) == "HOT"
    assert comfort_level(40) == "HOT"
