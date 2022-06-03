from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Gleb")
    browser.find_element(By.NAME, "lastname").send_keys("Kudinov")
    browser.find_element(By.NAME, "email").send_keys("t@t.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty.txt')
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
except Exception as errors:
    print(f"Errors in this scope {errors}")
finally:
    time.sleep(5)
    browser.quit()
