from selenium.webdriver.common.by import By
import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_basket_form(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.XPATH, "//*[@id='add_to_basket_form']/button")
    assert button, "Кнопка не найдена"