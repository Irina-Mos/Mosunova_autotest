import pytest
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



def test_get_book(close_session):
    # alert = driver.switch_to.alert
    # alert.accept()
    search = driver.find_element(By.XPATH, "//input[@class='_60b66d7d']")
    search.click()
    search.send_keys("Пушкин")
    search_button = driver.find_element(By.CLASS_NAME, "_43bac248")
    search_button.click()
    page_title = driver.find_element(By.CLASS_NAME, "c62fbeb9")
    text_title = page_title.text
    assert text_title.lower() == "результаты поиска «пушкин»"
    book_list = []
    for i in range(0, 5):
        book = driver.find_element(By.CLASS_NAME, "d14d2f6b")
        book_list.append(book.text)

    print(book_list)
    driver.quit()