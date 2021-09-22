from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
from send_answer import send_answer
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element_by_css_selector('button[class="trollface btn btn-primary"')
    input1.click()

    print(browser.current_window_handle)
    print(browser.window_handles)
    window2 = browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input2 = browser.find_element_by_css_selector('input[class="form-control"]')
    input2.send_keys(y)

    button = browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    answer = browser.switch_to.alert.text.split()[-1]
    send = input(f'Отослать ответ: {answer}? Y/N')
    if send in ['Y', 'y', 'Н', 'н']: send_answer(answer, 'https://stepik.org/lesson/184253/step/6?unit=158843')
    time.sleep(5)
    browser.quit()
