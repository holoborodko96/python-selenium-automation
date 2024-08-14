from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open page target.com')
def open_target(context):
    context.driver.get("https://www.target.com/")

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[text()='Sign in']").click()

@when('From right side navigation menu, click Sign In')
def nav_menu_click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[text()='Sign in']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text=context.driver.find_element(By.XPATH, "//span[text()='Sign into your target account']")
    assert 'Sign into your target account' in actual_text
    print('Test case passed')