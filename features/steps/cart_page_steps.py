from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.CSS_SELECTOR, '[class*="CartSummarySpan"]')


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart, f'Expected {amount} item(s) but got {cart}'

