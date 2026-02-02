from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("http://perm.top-academy.ru/")
text = "Академия Топ"
element = chrome.find_element(by="xpath", value=f"//span[text() = '{text}']")
chrome.quit()

