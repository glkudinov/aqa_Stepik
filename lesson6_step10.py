from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    dictionary = (
        {"css": "input[placeholder='Input your first name']", "text": "Gleb"},
        {"css": "input[placeholder='Input your last name']", "text": "Kudinov"},
        {"css": "input[placeholder='Input your email']", "text": "test@mail.ru"}
    )

    for element in dictionary:
        textarea = browser.find_element(By.CSS_SELECTOR, element["css"])
        textarea.send_keys(element["text"])

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(5)
    welcome_text = browser.find_element(By.CSS_SELECTOR, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text
except Exception as errors:
    print(f"Errors in this scope {errors}")
finally:
    time.sleep(5)
    browser.quit()
