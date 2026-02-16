import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_tab(driver):
    with allure.step('Проверка переключения между вкладками. Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Нажимаем на вкладку "Пиццы".'):
        # pizza = driver.find_element(By.XPATH, "//a[@class = 'sc-1c0ft0g-0 jndbbS sc-1uavg9b-7 cONjBT']")

        vklads = driver.find_elements(By.XPATH, "//a[@class='sc-1c0ft0g-0 jndbbS sc-1uavg9b-7 cONjBT']")
        for vklad in vklads:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vklad)
            vklad.click()
            print(vklad.text)
            time.sleep(3)

