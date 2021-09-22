# можно запустить так тк pytest совместим с unittest
# pytest -v --tb=line 331pytest.py

import unittest

from selenium import webdriver
import time, random


def test_1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_2():
    assert abs(-42) == -42, "Should be absolute value of a number"


class TestAbs(unittest.TestCase):
    def test_3(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        for placeholder in ["Input your first name", "Input your last name", "Input your email"]:
            word = random.sample(list("aaaaaqwrtooooooyuiooopsdfghjuuuuklzxcvbeeeeeeeenm"), random.randint(5, 10))
            browser.find_element_by_css_selector(f'[placeholder="{placeholder}"]').send_keys(word)
            time.sleep(1)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        time.sleep(3)
        browser.quit()

    def test_4(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        for placeholder in ["Input your first name", "Input your last name", "Input your email"]:
            word = random.sample(list("aaaaaqwrtooooooyuiooopsdfghjuuuuklzxcvbeeeeeeeenm"), random.randint(5, 10))
            browser.find_element_by_css_selector(f'[placeholder="{placeholder}"]').send_keys(word)
            time.sleep(1)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        time.sleep(3)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
