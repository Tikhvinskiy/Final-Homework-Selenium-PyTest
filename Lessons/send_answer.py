from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_answer(answer, link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    email = '######@mail.ru'
    password = '#######'

    browser.get(link)
    promo = WebDriverWait(browser, 5).until(EC.url_changes(link))
    current_url = browser.current_url + '?auth=login'
    if promo:
        browser.get(current_url)
        browser.find_element_by_css_selector('[name = "login"]').send_keys(email)
        browser.find_element_by_css_selector('[name = "password"]').send_keys(password)
        browser.find_element_by_css_selector(".sign-form__btn").click()
    WebDriverWait(browser, 5).until(EC.url_changes(current_url))
    browser.get(link)
    right = browser.find_element_by_css_selector('div[data-type="string-quiz"]').get_attribute('data-state')
    if right == 'no_submission':
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    else:
        browser.find_element_by_css_selector('button[class="again-btn white"]').click()
        browser.find_element_by_css_selector('footer[class="modal-popup__footer ember-view"] :first-child').click()
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    browser.find_element_by_css_selector('button[class ="submit-submission"]').click()
