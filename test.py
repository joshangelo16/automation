from selenium import webdriver
from selenium.webdriver.common.by import By
import pygetwindow as gw
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://joshangelo.vercel.app/")
time.sleep(2)

# Click email link
email = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto')]")
email.click()
time.sleep(4)  # Wait for Outlook to open

# Print all open window titles
print(gw.getAllTitles())

driver.quit()