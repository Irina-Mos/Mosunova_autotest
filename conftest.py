import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    chrome = webdriver.Edge()
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()