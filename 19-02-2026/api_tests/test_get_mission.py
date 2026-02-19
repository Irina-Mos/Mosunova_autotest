import requests

url_mis = "https://osdr.nasa.gov/geode-py/ws/api/missions"

def test_get_mission():
    try:
        response = requests.get(url_mis)
    except requests.exceptions.RequestException as e:
        print(f'Не смогли получить миссию, ошибка {e}')
        raise
    my_json = response.json()
    missions = my_json.get('data')
    l = len(missions)
    counter = 0
    for mis in missions:
        mis_num = mis["mission"]
        if "STS" in mis_num:
            counter += 1
    assert l == 158
    print(f"Количество миссий STS: {counter}")
    assert response.status_code == 200