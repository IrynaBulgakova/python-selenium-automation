from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')

    def search_results(self, expected_result):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_result in actual_text, f"Expected {expected_result} is not in {actual_text}"



