from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    MESSAGE = (By.XPATH, '//div[@data-test="boxEmptyMsg"]')
    CART_SUMMARY = (By.CSS_SELECTOR, '[class*="CartSummarySpan"]')

    def verify_message_is_shown(self, *locator):
        actual_text = self.driver.find_element(*self.MESSAGE).text
        assert "Your cart is empty" in actual_text, f'Message "Your cart is empty" not in {actual_text}'
        print('Test case passed')

    def open_cart_page(self):
        self.open('https://www.target.com/cart')

    def verify_cart_items(self, amount):
        cart = self.driver.find_element(*self.CART_SUMMARY).text
        assert amount in cart, f'Expected {amount} item(s) but got {cart}'