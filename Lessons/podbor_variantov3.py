from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click(s):
    WebDriverWait(browser, waiting).until(EC.element_to_be_clickable((By.CSS_SELECTOR, s)))
    browser.find_element_by_css_selector(s).click()


def clickxpath(s):
    WebDriverWait(browser, waiting).until(EC.element_to_be_clickable((By.XPATH, s)))
    browser.find_element_by_xpath(s).click()


def send(s, keys):
    WebDriverWait(browser, waiting).until(EC.element_to_be_clickable((By.CSS_SELECTOR, s)))
    browser.find_element_by_css_selector(s).send_keys(keys)


def nl(n):
    return (variants + 2 - len(bin(n))) * "0" + bin(n)[2:]


def c(n=0):
    global not_made
    WebDriverWait(browser, waiting).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    while True:
        n += 1
        es = []
        c = nl(n)
        if len(str(c).replace('0', '')) < 4:
            # print(c, len(str(c).replace('0', '')))
            continue
        print(n, c, len(str(c).replace('0', '')))
        for i in range(variants):
            if c[i] == "1":
                es.append(s[i])
        for i in es:
            try:
                clickxpath(i)
            except Exception as E:
                print(E)
                not_made.append(n)
                f = open("errors.txt", "wb")
                pickle.dump(not_made, f)
                f.close()
                break

        click(".submit-submission")
        time.sleep(1.5)
        try:
            result = browser.find_element_by_css_selector(".attempt__score-info").text
            if "Вы получили" in result:
                print('Готово! Ответы:')
                for i in es:
                    print(i[21:-2])
                return
        except Exception:
            pass

        click(".again-btn")
        time.sleep(1.5)
        if n >= 2 ** variants:
            return print("The End")


def ss(lesson):
    browser.get(lesson)
    time.sleep(3)
    browser.execute_script("window.scrollBy(0, 300);")
    c()


not_made = []
waiting = 20
browser = webdriver.Chrome()
browser.implicitly_wait(5)
email = '###@mail.ru'
password = '#######'
lesson = 'https://stepik.org/lesson/34823/step/8?unit=14256'
enter_link = "https://stepik.org/catalog?auth=login"
browser.get(enter_link)
send('[name = "login"]', email)
send('[name = "password"]', password)
click(".sign-form__btn")
time.sleep(3)
s = ['//*[contains(text(), "из B=>A и (не А) следует (не В)")]',
     '//*[contains(text(), "из (А=>(B=>C)) следует ((A=>B)=>C)")]',
     '//*[contains(text(), "из (A=>B) и (A=> (не B)) следует (не A)")]',
     '//*[contains(text(), "из В=>A и (не В) следует (не А)")]',
     '//*[contains(text(), "из A=>B и (не B) следует (не A)")]',
     '//*[contains(text(), "из (A=>B) и (B=>C) следует (A=>C)")]',
     '//*[contains(text(), "из (A=>(B=>C)) следует (B=>(A=>C))")]']
variants = len(s)
ss(lesson)

f = open("errors.txt", "rb")
print(pickle.load(f))
