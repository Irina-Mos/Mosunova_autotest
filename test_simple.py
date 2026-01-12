import pytest


def test_simple_1():
    assert 2+2 == 4, "2+2 должно быть 4, а не 5"

@pytest.mark.regress #тесты для регрессионных проверок
@pytest.mark.parametrize("a, b, expected_value", [
    (2, 2, 4),
    (2, 2, 0),
    (5, 5, 10),
    (5, 5, 5)
])

def test_simple(a, b, expected_value):
    assert a + b == expected_value, f"{a} + {b} получилось {expected_value}"

def test_summ_number(get_data):
    data = get_data
    assert data["a"] + data["b"] == 7

@pytest.mark.connection
def test_connection(setup_and_teardowm):
    assert setup_and_teardowm["connect"] == True

@pytest.mark.connection
def test_connection_1(setup_and_teardowm):
    assert setup_and_teardowm["connect"] == True

