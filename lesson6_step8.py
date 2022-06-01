from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)
try:
    dictionary = (
        {"css": "input[name='first_name']", "text": "Gleb"},
        {"css": "input[name='last_name']", "text": "Kudinov"},
        {"css": ".city", "text": "Simferopol"},
        {"css": "#country", "text": "Russia"}
    )

    for element in dictionary:
        textarea = browser.find_element(By.CSS_SELECTOR, element["css"])
        textarea.send_keys(element["text"])
    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
except Exception as errors:
    print(f"Errors in this scope {errors}")
finally:
    time.sleep(10)
    browser.quit()
