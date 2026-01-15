import pytest
from auth_tests.auth_simple.auth import login

@pytest.mark.user
@pytest.mark.parametrize("username, password", [
    ("admin","admin123"),
    ("Irina","Irina123"),
    ("rollandsushi","8roll1sushi"),
    ("guest","guest"),
    ("admin","admin124")
                         ])
def tests(username, password):
    assert login(username, password)


@pytest.fixture()
def get_user():
    return {
        "valid_user_1": {"username": "admin", "password": "admin123"},
        "invalid_user_1": {"username": "Irina", "password": "Irina124"},
        "invalid_user_2": {"username": "admin", "password": "admin121"},
        "valid_user_2": {"username": "guest", "password": "guest"}
    }
@pytest.mark.user
def tests_1(get_user):
    user = get_user.get("valid_user_1")
    assert login(user.get("username"), user.get("password"))
@pytest.mark.user
def tests_2(get_user):
    user = get_user.get("invalid_user_1")
    assert login(user.get("username"), user.get("password"))
@pytest.mark.user
def tests_3(get_user):
    user = get_user.get("valid_user_2")
    assert login(user.get("username"), user.get("password"))
@pytest.mark.user
def tests_4(get_user):
    user = get_user.get("invalid_user_2")
    assert login(user.get("username"), user.get("password"))

