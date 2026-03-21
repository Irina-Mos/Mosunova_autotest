import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_tab(driver):
    with allure.step('Проверка переключения на страницу "Доедешь-напиши". Выбор выпуска шоу. Открываем сайт "Яндекс Путешествия".'):
        driver.get("https://travel.yandex.ru/avia/")
    with allure.step('Нажимаем на вкладку "Журнал путешествий".'):
        journal = driver.find_element(By.XPATH, "//a[@href = 'https://travel.yandex.ru/journal/']")
        journal.click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
    with allure.step('Нажимаем на вкладку "Доедешь-Напиши".'):
        go_write = driver.find_element(By.XPATH, "//a[@href = '/journal/category/doedesh-napishi/']")
        go_write.click()
    with allure.step('Выбираем выпуск шоу "Москва".'):
        series = driver.find_element(By.XPATH, "//button[@class = 'RJee8 zs6al bZTEr Wiaor nVIrU']")
        series.click()
        moscow = driver.find_element(By.XPATH, "//a[@href = '/journal/doedesh-napishi-s2-e4/']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", moscow)
        moscow.click()
