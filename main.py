from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://joshangelo.vercel.app/")
print("Title:", driver.title)

# Click nav links
driver.find_element(By.XPATH, "//a[@href='#about']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[@href='#projects']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[@href='#contact']").click()
time.sleep(1)

# Project open button ID + close button ID
projects = [
    ("Restaurant Website",     "openRestaurantModal",  "restaurantModal"),
    ("Web Application (SaaS)", "openWebAppModal",      "webapplicationModal"),
    ("Progressive Web App",    "openProgressiveModal", "progressiveModal"),
    ("E-Commerce Website",     "openEcommerceModal",   "ecommerceModal"),
]

for project, open_id, close_id in projects:
    print(f"Opening: {project}")

    # Open modal
    btn = wait.until(EC.element_to_be_clickable((By.ID, open_id)))
    btn.click()
    time.sleep(2)
    print(f"  Modal opened!")

    # Close modal
    close_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//*[@id='{close_id}']/div/button")
    ))
    close_btn.click()
    time.sleep(1)
    print(f"  Modal closed.")

# About section
driver.find_element(By.XPATH, "//a[@href='#about']").click()
time.sleep(1)

about_text = driver.find_element(By.XPATH, "//section[@id='about'] | //div[@id='about']").text
print("About text found:", about_text[:60], "...")

assert "Josh" in about_text, "Name not found in About section"
assert "Quality Assurance" in about_text, "QA text not found"
print("About section verified!")

# Contact section
driver.find_element(By.XPATH, "//a[@href='#contact']").click()
time.sleep(1)

# Click email link
email = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto')]")
print("Email:", email.get_attribute("href"))
time.sleep(4)

# Switch back to Chrome
driver.switch_to.window(driver.current_window_handle)
time.sleep(1)
print("Email:", email.get_attribute("href"))

# LinkedIn - need correct XPath
linkedin = driver.find_element(By.XPATH, "//a[contains(@href, 'linkedin')]")
print("LinkedIn:", linkedin.get_attribute("href"))

github = driver.find_element(By.XPATH, "//a[contains(@href, 'github')]")
print("GitHub:", github.get_attribute("href"))

# Screenshots
driver.save_screenshot("portfolio_homepage.png")

driver.find_element(By.XPATH, "//a[@href='#about']").click()
time.sleep(1)
driver.save_screenshot("portfolio_about.png")

driver.quit()
print("Done!")







