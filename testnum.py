from number import number

def test_positive_numbers():
    result = calculator(10, 5)
    assert result["addition"] == 15
    assert result["subtraction"] == 5
    assert result["multiplication"] == 50
    assert result["division"] == 2

def test_negative_numbers():
    result = calculator(-8, 2)
    assert result["addition"] == -6
    assert result["subtraction"] == -10
    assert result["multiplication"] == -16
    assert result["division"] == -4

def test_decimal_numbers():
    result = calculator(5.5, 2.2)
    assert result["addition"] == 7.7
    assert result["division"] == 2.5

def test_division_by_zero():
    result = calculator(10, 0)
    assert result["division"] is None
