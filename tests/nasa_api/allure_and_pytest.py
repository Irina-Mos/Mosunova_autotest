import allure
import pytest
import requests
from framework.helpers import some_help_function

@allure.id("1")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get experiment from nasa_api")
@allure.description("Test get experiment from nasa_api")
# @allure.testcase("")

@pytest.mark.nasa_tests

@pytest.mark.skip(reason="Метод полученияи экспериментов не работает")
@pytest.mark.skipif(a = 2, reason="Пропустить тест, если переменная a = 2")
@pytest.mark.parametrize("language", ["eng", "uz", "kz"])
def test_get_experiment():
    pass
    requests.get(f"http://get_language")
    with allure.step("Step 1"):
        pass