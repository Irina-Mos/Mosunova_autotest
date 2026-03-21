import allure
import pytest
import requests

url_veh = "https://osdr.nasa.gov/geode-py/ws/api/vehicles"

@allure.id("005")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get vehicles from nasa_api")
@allure.description("Finding a vehicle named Apollo")
@pytest.mark.nasa_tests
def test_get_vehicle():
    with allure.step("Выполняем переход по url."):
        try:
            response = requests.get(url_veh)
        except requests.exceptions.RequestException as e:
            print(f'Не смогли получить транспорт, ошибка {e}')
            raise
    with allure.step('Находим транспорт "Apollo"'):
        my_json = response.json()
        vehicles = my_json.get('data')
        l = len(vehicles)
        flag = False
        for vehicle in vehicles:
            veh_num = vehicle["vehicle"]
            if "Apollo" in veh_num:
                flag = True
        assert flag
        assert l == 24
        assert response.status_code == 200