from selenium import webdriver
import time
import math
import pytest
from send_answer import send_answer

message = ''
lessons = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope="session")
def browser():
    global message
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    print(message)
    send_answer(message, 'https://stepik.org/lesson/237240/step/3?unit=209628')
    browser.quit()


@pytest.mark.parametrize('link', lessons)
def test_ufo(browser, link):
    global message
    browser.get(link)
    browser.implicitly_wait(5)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('textarea').send_keys(answer)
    browser.find_element_by_css_selector('button[class="submit-submission"]').click()
    correct = browser.find_element_by_css_selector('pre[class="smart-hints__hint"]').text
    if correct != 'Correct!':
        message += correct
    assert correct == 'Correct!', 'Message is not correct'
