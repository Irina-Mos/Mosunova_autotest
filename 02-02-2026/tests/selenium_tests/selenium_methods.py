from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//div[text() = 'Hello']")

element = driver.find_element()

element.click()

element.send_keys()

element.clear()

element.submit()

windows = driver.window_handles

driver.switch_to.window(windows[0])

driver.switch_to.frame(windows[1])

driver.switch_to.default_content()

driver.implicitly_wait(5)

# WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())

title = driver.title

current_url = driver.current_url

page_source = driver.page_source

element_attrs = element.get_attribute("class")


alert = driver.switch_to.alert
alert.accept()
alet.dismiss()
alert.send_keys(Keys.RETURN)
text = alert.text

driver.get_screenshot_as_png()
driver.get_screenshot_as_file("my_screenshot.png")