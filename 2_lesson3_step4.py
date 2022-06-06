from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    answer = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
except Exception as errors:
    print(f"Errors in this scope {errors}")
finally:
    time.sleep(10)
    browser.quit()
