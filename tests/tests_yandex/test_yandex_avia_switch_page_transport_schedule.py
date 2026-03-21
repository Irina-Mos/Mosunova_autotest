import allure
import pytest
from selenium.webdriver.common.by import By

@allure.id("002")
@allure.feature("Yandex avia")
@allure.label("Api test")
@allure.title('Переход на страницу "Расписание транспорта"')
@allure.description('Проверка перехода на страницу "Расписание транспорта"')
@pytest.mark.yandex_tests

def test_tab(driver):
    with allure.step('Открываем сайт "Яндекс Путешествия".'):
        driver.get("https://travel.yandex.ru/avia/")
    with allure.step('Нажимаем на вкладку "Расписание транспорта".'):
        table = driver.find_element(By.XPATH, "//a[@href = 'https://rasp.yandex.ru/']")
        table.click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
    with allure.step('Проверяем, что перешли на страницу "Расписание транспорта".'):
        title = driver.find_element(By.XPATH, "//h1")
        text = title.text
        expected_title = "Расписание пригородного и междугородного транспорта"
        assert text == expected_title