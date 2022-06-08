import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc():
    return math.log(int(time.time()))


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_pages_for_search_the_answer(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    text_area = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area")))
    answer = calc()
    text_area.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    attempt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    msg = attempt.text
    assert msg == "Correct!", f"Answer is incorrect, got message '{msg}'"



