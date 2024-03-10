from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.side_navigation_page import SideNavigationPage
from pages.log_in_page import LogInPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.log_in_page = LogInPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_navigation_page = SideNavigationPage(driver)
