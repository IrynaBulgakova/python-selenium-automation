from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_on_icon(self, *locator):
        self.driver.find_element(*self.CART_ICON).click()



        
