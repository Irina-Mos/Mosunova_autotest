import allure
import pytest
import requests

url_exp = "https://osdr.nasa.gov/geode-py/ws/api/experiments"

@allure.id("002")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get experiments from nasa_api")
@allure.description("Output of experiment names")
@pytest.mark.nasa_tests
def test_get_experiment():
    with allure.step("Выполняем переход по url."):
        try:
            response = requests.get(url_exp)
        except requests.exceptions.RequestException as e:
            print(f'Не смогли получить эксперимент, ошибка {e}')
            raise
    with allure.step("Вывод названий экспериментов."):
        my_json = response.json()
        experiments = my_json.get('data')
        for exp in experiments:
            exp_num = exp["experiment"]
            print(exp_num[-6:])
        print(response.status_code)
        assert response.status_code == 200

