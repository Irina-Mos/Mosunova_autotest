import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_tab(driver):
    driver.get("https://travel.yandex.ru/avia/")
    hotels = driver.find_element(By.XPATH, "//a[@href = '/hotels/']")
    hotels.click()
    expected_hex = "#ff2f5f"
    time.sleep(1)
    text_color_hotels = Color.from_string(hotels.value_of_css_property('color')).hex.lower()
    assert expected_hex == text_color_hotels
    print(text_color_hotels)
    avia = driver.find_element(By.XPATH, "//a[@href = '/avia/']")
    avia.click()
    time.sleep(1)
    text_color_avia = Color.from_string(avia.value_of_css_property('color')).hex.lower()
    assert expected_hex == text_color_avia
    print(text_color_avia)