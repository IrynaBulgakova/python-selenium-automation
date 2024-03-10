from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.CSS_SELECTOR, '[class*="CartSummarySpan"]')


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.open_cart_page()


@then('Verify that cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)

