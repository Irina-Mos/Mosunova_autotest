import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://perm.top-academy.ru/")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope="function")
def close_session():
    yield
    driver.quit()

def test_get_text(close_session):
    children_button = driver.find_element(By.CSS_SELECTOR, "a.top-nav-item.top-nav-item-accent")
    children_button.click()

    page_title = driver.find_element(By.XPATH, "//h1[contains(text(), 'для детей')]")
    text_title = page_title.text
    assert text_title.lower() == "компьютерное образование для детей в перми"