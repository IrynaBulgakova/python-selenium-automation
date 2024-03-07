from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    MESSAGE = (By.XPATH, '//div[@data-test="boxEmptyMsg"]')

    def verify_message_is_shown(self, *locator):
        actual_text = self.driver.find_element(*self.MESSAGE).text
        assert "Your cart is empty" in actual_text, f'Message "Your cart is empty" not in {actual_text}'
        print('Test case passed')