import requests
import allure
import pytest
url = "https://osdr.nasa.gov/geode-py/ws/api/subjects"
@allure.id("2")
@allure.feature("NASA API")
@allure.label("Api test")
@allure.title("Get subjects from nasa_api")
@allure.description("Finding subject number 195")
@pytest.mark.nasa_tests
def test_get_subject():
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'Не смогли получить объекты, ошибка {e}')
        raise
    my_json = response.json()
    subjects = my_json.get('data')
    for subj in subjects:
        val = 'https://osdr.nasa.gov/geode-py/ws/api/subject/195'
        if subj.get("subject") == val:
            subj_response = requests.get(val)
            print(subj_response.json())
            print(subj_response.status_code)
            assert subj_response.status_code == 200
    print(response.status_code)
    assert response.status_code == 200
