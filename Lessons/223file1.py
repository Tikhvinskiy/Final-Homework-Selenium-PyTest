from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
from send_answer import send_answer
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys('An1')

    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys('An2')

    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys('An3')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    open(file_path, 'a').close()
    input4 = browser.find_element_by_css_selector('input[id="file"]')
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector('button[class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    answer = browser.switch_to.alert.text.split()[-1]

finally:
    send = input(f'Отослать ответ: {answer}? Y/N')
    if send in ['Y','y','Д','д']: send_answer(answer, 'https://stepik.org/lesson/228249/step/8?unit=200781')
    time.sleep(5)
    browser.quit()