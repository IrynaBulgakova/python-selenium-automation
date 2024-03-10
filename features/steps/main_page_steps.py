from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
NAV_MENU_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')
SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, '[data-test="resultsHeading"]')


@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are {expected_amount} benefit boxes')
def verify_benefit_boxes(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == expected_amount, f"Expected {expected_amount} benefit boxes, but {len(benefit_boxes)} are shown"


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Search results for {expected_result} are shown')
def search_results(context, expected_result):
    context.app.search_results_page.search_results(expected_result)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.main_page.click_add_to_cart()


@when('Click from navigation menu on Add to Cart button')
def click_nav_menu_add_to_cart(context):
    context.app.side_navigation_page.click_nav_menu_add_to_cart()



