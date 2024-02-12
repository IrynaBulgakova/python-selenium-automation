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

driver.get("https://bit.ly/4bw0V4r")
sleep(5)
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']") #Amazon logo search by XPATH
driver.find_element(By.ID,"ap_email") #email field search by ID
driver.find_element(By.XPATH,"//input[@type='submit']") #continue button search by XPATH
driver.find_element(By.XPATH,"//a[contains(@href,'ref=ap_signin_notification_condition_of')]") #condition of use
driver.find_element(By.XPATH,"//a[contains(@href,'notification_privacy')]")#privacy notice
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']") #need help link
driver.find_element(By.ID, "createAccountSubmit") #create your Amazon account link by ID
print("success")
