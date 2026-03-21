import allure
import pytest
import requests

url_mis = "https://osdr.nasa.gov/geode-py/ws/api/missions"

@allure.id("003")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get missions from nasa_api")
@allure.description('Output of "STS" missions')
@pytest.mark.nasa_tests
def test_get_mission():
    with allure.step("Выполняем переход по url."):
        try:
            response = requests.get(url_mis)
        except requests.exceptions.RequestException as e:
            print(f'Не смогли получить миссию, ошибка {e}')
            raise
    with allure.step('Поиск миссий "STS".'):
        my_json = response.json()
        missions = my_json.get('data')
        counter = 0
        for mis in missions:
            mis_num = mis["mission"]
            if "STS" in mis_num:
                counter += 1
        print(f"Количество миссий STS: {counter}")
        assert response.status_code == 200