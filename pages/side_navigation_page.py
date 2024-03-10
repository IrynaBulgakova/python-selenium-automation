from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SideNavigationPage(Page):
    NAV_MENU_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    NAV_MENU_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')

    def click_from_navigation_menu_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.NAV_MENU_SIGN_IN)).click()

    def click_nav_menu_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.NAV_MENU_ADD_TO_CART_BTN)).click()