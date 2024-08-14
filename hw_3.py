from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26pd_rd_w%3D0129n%26content-id%3Damzn1.sym.8b17d5d4-f780-4476-bbb4-5d216813632d%26pf_rd_p%3D8b17d5d4-f780-4476-bbb4-5d216813632d%26pf_rd_r%3D9H198EDEN0ESN5K1FN2P%26pd_rd_wg%3DqtTsy%26pd_rd_r%3D631aa50d-bb60-49b3-ae83-cba17c3bbe8f&openid.assoc_handle=anywhere_v2_us')
#locator for Amazon logo
driver.find_element(By.CSS_SELECTOR,"i.a-icon.a-icon-logo")
#locator for "Create account" header
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
#locator for "Your name" field
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")
#locator for "Mobile number or Email" field
driver.find_element(By.CSS_SELECTOR,"input[data-validation-id='email']")
#locator for "Password" field
driver.find_element(By.CSS_SELECTOR,"#ap_password")
#locator for "Passwords must be at least 6 characters" text
driver.find_element(By.XPATH,"//div[text()='Passwords must be at least 6 characters.']")
#locator for re-enter password field
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
#locator for "Create amazon account" button
driver.find_element(By.CSS_SELECTOR,"input[aria-labelledby='a-autoid-0-announce']")
#locator for Conditions of use link
driver.find_element(By.CSS_SELECTOR,"a[href*='condition_of_use']")
#locator for Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice' and text()='.']")
#locator for sign in link
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")