import time
from selenium.webdriver.common.by import By
def test_add_to_basket_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(30) 
    
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Button 'Add to basket' is not displayed!"