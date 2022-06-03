from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = ["http://suninjuly.github.io/selects1.html", "http://suninjuly.github.io/selects2.html"]
    browser = webdriver.Chrome()
    browser.get(link[0])
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    select_elt = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select_elt.select_by_value(str(num1 + num2))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
except Exception as errors:
    print(f"Errors in this scope {errors}")
finally:
    time.sleep(2)
    browser.quit()
