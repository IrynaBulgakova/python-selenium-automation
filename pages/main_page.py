from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')

    def open_main(self):
        self.open('https://www.target.com/')

    def click_add_to_cart(self, *locator):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()
