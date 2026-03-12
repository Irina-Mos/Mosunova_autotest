from pages.page_login import LoginPage

def test_auth(driver):
    login = LoginPage(driver)

    login.open()
    login.enter_email("")
    login.enter_password("")
    login.click_login()

    login.check_enter_text()
    assert login.check_enter_text() == "Добро пожаловать"