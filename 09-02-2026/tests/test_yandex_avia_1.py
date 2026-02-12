import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_tab(driver):
    with allure.step('Проверка переключения между вкладками. Открываем сайт "Яндекс Путешествия".'):
        driver.get("https://travel.yandex.ru/avia/")
    with allure.step('Нажимаем на вкладку "Отели".'):
        hotels = driver.find_element(By.XPATH, "//a[@href = '/hotels/']")
        hotels.click()
    with allure.step('Определяем цвет вкладки "Путешествия".'):
        expected_hex = "#f00044"
        time.sleep(1)
        text_color_hotels = Color.from_string(hotels.value_of_css_property('color')).hex.lower()
    with allure.step('Сверяем текущий цвет вкладки "Путешествия" с заданным.'):
        assert expected_hex == text_color_hotels
        print(text_color_hotels)

    with allure.step('Нажимаем на вкладку "Авиа".'):
        avia = driver.find_element(By.XPATH, "//a[@href = '/avia/']")
        avia.click()
    with allure.step('Определяем цвет вкладки "Авиа".'):
        time.sleep(1)
        text_color_avia = Color.from_string(avia.value_of_css_property('color')).hex.lower()
    with allure.step('Сверяем текущий цвет вкладки "Авиа" с заданным.'):
        assert expected_hex == text_color_avia
        print(text_color_avia)

    with allure.step('Нажимаем на вкладку "Ж/д".'):
        trains = driver.find_element(By.XPATH, "//a[@href = '/trains/']")
        trains.click()
    with allure.step('Определяем цвет вкладки "Ж/д".'):
        time.sleep(1)
        text_color_trains = Color.from_string(trains.value_of_css_property('color')).hex.lower()
    with allure.step('Сверяем текущий цвет вкладки "Ж/д" с заданным.'):
        assert expected_hex == text_color_trains
        print(text_color_trains)

    with allure.step('Нажимаем на вкладку "Туры".'):
        tours = driver.find_element(By.XPATH, "//a[@href = '/tours/']")
        tours.click()
    with allure.step('Определяем цвет вкладки "Туры".'):
        time.sleep(1)
        text_color_tours = Color.from_string(tours.value_of_css_property('color')).hex.lower()
    with allure.step('Сверяем текущий цвет вкладки "Туры" с заданным.'):
        assert expected_hex == text_color_tours
        print(text_color_tours)