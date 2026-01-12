import pytest

@pytest.fixture()
def get_data():
    return {"a": 2,
            "b": 5}

@pytest.fixture(scope="function")
def setup_and_teardowm():
    print("Подготовка соединения")
    resource = {
        "connect": True
    }
    yield resource
    print("Разрыв соединения")
    resource["connect"] = False