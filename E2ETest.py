import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

productsList = []
# Capture products on the page
products = driver.find_elements(By.XPATH, "(//div[@class='card h-100'])")
count = len(products)
print(count)
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("america")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']")))
driver.find_element(By.PARTIAL_LINK_TEXT, "America").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[type*='submit']").click()
SuccessText = driver.find_element(By.CLASS_NAME, "alert-success").text
print(SuccessText)
assert "Success!" in SuccessText

