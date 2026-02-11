import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_tab(driver):
    driver.get("https://travel.yandex.ru/avia/")
    table = driver.find_element(By.XPATH, "//a[@href = 'https://rasp.yandex.ru/']")
    table.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    title = driver.find_element(By.XPATH, "//h1")
    text = title.text
    expected_title = "Расписание пригородного и междугородного транспорта"
    assert text == expected_title