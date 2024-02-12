from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://amzn.to/3urwf3i')
driver.find_element(By.CSS_SELECTOR, '#nav-logobar')  #Amazon logo CSS by ID
driver.find_element(By.CSS_SELECTOR, '.a-size-base.a-text-bold') #Create account and Sign in  CSS by class
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name') #Name by ID
driver.find_element(By.CSS_SELECTOR, '#ap_email') #email by ID
driver.find_element(By.CSS_SELECTOR,'#ap_password') #password by ID
driver.find_element(By.CSS_SELECTOR,'[aria-labelledby="auth-continue-announce"]') #Continue instead of create
driver.find_element(By.CSS_SELECTOR,'[href*="register_notification_condition"]') #Condition of use by attribute
driver.find_element(By.CSS_SELECTOR,'[href*="privacy_notice"]') #Privacy Notice by attribute
sleep(2)
print("elements were located")


