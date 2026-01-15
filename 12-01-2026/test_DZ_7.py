import pytest

@pytest.mark.operation
@pytest.mark.parametrize("a, b, expected_value", [
    (2, 2, 4),
    (2, 2, 1),
    (5, 5, 1),
    (5, 5, 25)
])

def test_multiplication(a, b, expected_value):
    assert a * b == expected_value, f"{a} * {b} = {expected_value}"

@pytest.mark.operation
@pytest.mark.parametrize("a, b, expected_value", [
    (2, 2, 4),
    (2, 2, 1),
    (5, 5, 1),
    (5, 5, 25)
])
def test_devision(a, b, expected_value):
    a / b == expected_value, f"{a} / {b} != {expected_value}"



