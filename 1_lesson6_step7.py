from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("answer")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

except Exception as errors:
    print(f"Errors when run {errors}")

finally:
    time.sleep(30)
    browser.quit()
