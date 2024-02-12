from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target.com')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="@web/CartIcon"]').click()
    sleep(4)

@then('Message Your cart is empty is shown')
def verify_message_is_shown(context):
    actual_text = context.driver.find_element(By.XPATH,'//div[@data-test="boxEmptyMsg"]').text
    assert "Your cart is empty" in actual_text, f'Message "Your cart is empty" not in {actual_text}'
    print('Test case passed')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    sleep(2)

@when('Click from navigation menu on Sign In')
def click_from_navigation_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]').click()
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'#username')
    print('Sign In form opened')