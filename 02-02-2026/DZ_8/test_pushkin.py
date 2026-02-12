import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.litres.ru")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope="function")
def close_session():
    yield
    driver.quit()



def test_get_book():
    # alert = driver.switch_to.alert
    # alert.accept()
    with allure.step("Выполняю первый шаг моего теста"):
        search = driver.find_element(By.XPATH, "//input[@class='_8fba8811']")
        search.click()
        search.send_keys("Пушкин")
        search_button = driver.find_element(By.XPATH, "//button[@class='_82b1c248']")
        search_button.click()
        page_title = driver.find_element(By.XPATH, "//h1[@class='c62fbeb9']")
        text_title = page_title.text
        assert text_title.lower() == "результаты поиска «пушкин»"
        books = driver.find_elements(By.XPATH, "//a[@class='d14d2f6b']")
        first_five_books = books[:5]
        for book in first_five_books:
            print(book.text)
        driver.quit()