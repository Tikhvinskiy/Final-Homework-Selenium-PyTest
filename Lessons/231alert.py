from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
from send_answer import send_answer
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element_by_css_selector('button[type="submit"]')
    input1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input2 = browser.find_element_by_css_selector('input[class="form-control"]')
    input2.send_keys(y)

    button = browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    answer = browser.switch_to.alert.text.split()[-1]

finally:
    send = input(f'Отослать ответ: {answer}? Y/N')
    if send in ['Y', 'y', 'Д', 'д']: send_answer(answer, 'https://stepik.org/lesson/228249/step/8?unit=200781')
    time.sleep(5)
    browser.quit()
