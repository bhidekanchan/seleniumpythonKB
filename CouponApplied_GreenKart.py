import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count) #(//div[@class='product'])[1]
veggies = []
for result in results:
    veggies.append( result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

print(veggies)
assert expectedlist == veggies

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//button[text()='PROCEED TO CHECKOUT'])").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

# Capture price of each veggie and calculate the total, compare it with the total amount displayed
prices = driver.find_elements(By.XPATH, "//td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

print(totalamt)

# Check for discounted amount and assert if it is lesser than the total amount

discounted_amt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(discounted_amt)
assert discounted_amt < totalamt