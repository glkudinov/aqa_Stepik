import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        dictionary = (
            {"css": "div.first_block div.first_class input", "text": "Gleb"},
            {"css": "div.first_block div.second_class input", "text": "Kudinov"},
            {"css": "div.first_block div.third_class input", "text": "test@mail.ru"}
        )

        for element in dictionary:
            textarea = browser.find_element(By.CSS_SELECTOR, element["css"])
            textarea.send_keys(element["text"])

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = browser.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fill all input!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        dictionary = (
            {"css": "div.first_block div.first_class input", "text": "Gleb"},
            {"css": "div.first_block div.second_class input", "text": "Kudinov"},
            {"css": "div.first_block div.third_class input", "text": "test@mail.ru"}
        )

        for element in dictionary:
            textarea = browser.find_element(By.CSS_SELECTOR, element["css"])
            textarea.send_keys(element["text"])

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = browser.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fill all input!")


if __name__ == "__main__":
    unittest.main()
