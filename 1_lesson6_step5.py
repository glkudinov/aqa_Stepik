import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/find_link_text"
find_name = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser = webdriver.Chrome()
browser.get(link1)
redirect_link = browser.find_element(By.LINK_TEXT, find_name)
redirect_link.click()

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

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

except Exception as errors:
    print(f"Возникли ошибки при выполнении {errors}")
finally:
    time.sleep(30)
    browser.quit()