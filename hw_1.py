from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')


# locator for Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# locator for Email field
driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']")
# locator for continue button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
# locator for Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# locator for privacy notice link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
# locator for Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# locator for Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')
# locator for Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
# locator for Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')