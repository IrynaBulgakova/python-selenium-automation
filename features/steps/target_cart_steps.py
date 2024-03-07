from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
SIGN_IN_ICON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
NAV_MENU_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


@given('Open Target.com')
def open_target_page(context):
    context.app.main_page.open_main()


@when('Click on cart icon')
def click_on_icon(context):
    context.app.header.click_on_icon()
    # context.driver.find_element(*CART_ICON).click()


@then('Message Your cart is empty is shown')
def verify_message_is_shown(context):
    context.app.cart_page.verify_message_is_shown()


@when('Click Sign In')
def click_sign_in(context):
    context.wait.until(EC.visibility_of_element_located(SIGN_IN_ICON)).click()
    # context.driver.find_element(*SIGN_IN_ICON).click()
    # sleep(2)


@when('Click from navigation menu on Sign In')
def click_from_navigation_menu_sign_in(context):
    context.wait.until(EC.presence_of_element_located(NAV_MENU_SIGN_IN)).click()
    # context.driver.find_element(*NAV_MENU_SIGN_IN).click()
    # sleep(2)


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '#username')
    print('Sign In form opened')