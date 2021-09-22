from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
from send_answer import send_answer

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"


try:
    browser.get(link)
    time.sleep(1)
    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_css_selector('input[class="form-check-input"][type="checkbox"]')
    input2.click()

    input3 = browser.find_element_by_css_selector('input[class="form-check-input"][id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()

    button = browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    answer = browser.switch_to.alert.text.split()[-1]
    print(answer)
    browser.quit()
    send_answer(answer, 'https://stepik.org/lesson/228249/step/6?unit=200781')
    time.sleep(5)
    browser.quit()