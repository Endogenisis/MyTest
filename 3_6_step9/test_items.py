from selenium.webdriver.common.by import By
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    message = browser.find_element(By.ID, "add_to_basket_form")
    assert "Добавить в корзину" in message.text