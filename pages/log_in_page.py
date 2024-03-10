from selenium.webdriver.common.by import By
from pages.base_page import Page


class LogInPage(Page):
    SIGN_IN_FORM = (By.CSS_SELECTOR, '#username')

    def verify_sign_in(self, *locator):
        self.driver.find_element(*self.SIGN_IN_FORM)
