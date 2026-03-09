import allure
import pytest
import requests

url_bio = "https://osdr.nasa.gov/geode-py/ws/api/biospecimen"


@allure.id("001")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get biospecimens from nasa_api")
@allure.description("Checking the quantity of biospecimens")
@pytest.mark.nasa_tests
def test_get_biospecimen():
    with allure.step("Выполняем переход по ошибочному url."):
        try:
            response = requests.get(url_bio)
        except requests.exceptions.RequestException as e:
            print(f'Не смогли получить биологический вид, ошибка {e}')
            raise
        assert response.status_code == 404
