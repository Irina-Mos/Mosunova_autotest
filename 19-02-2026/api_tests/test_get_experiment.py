import requests

url_exp = "https://osdr.nasa.gov/geode-py/ws/api/experiments"

def test_get_experiment():
    try:
        response = requests.get(url_exp)
    except requests.exceptions.RequestException as e:
        print(f'Не смогли получить эксперимент, ошибка {e}')
        raise
    my_json = response.json()
    experiments = my_json.get('data')
    l = len(experiments)
    for exp in experiments:
        exp_num = exp["experiment"]
        print(exp_num[-6:])
    assert l == 928
    print(response.status_code)
    assert response.status_code == 200

