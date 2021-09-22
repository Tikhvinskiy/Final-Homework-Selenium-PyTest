from selenium import webdriver
import time

browser = webdriver.Chrome()

email = '#####@mail.ru'
password = '#######'

browser.get("https://stepik.org/course/95/promo?auth=login")
time.sleep(3)


def click(s):
    browser.find_element_by_css_selector(s).click()


def send(s, keys):
    browser.find_element_by_css_selector(s).send_keys(keys)


send('[name = "login"]', email)
send('[name = "password"]', password)
click(".sign-form__btn")
time.sleep(1)


def nl(n):
    return (10 - len(bin(n))) * "0" + bin(n)[2:]


def c(n=0, num=0):
    while True:
        n += 1
        # print(n)
        es = []
        c = nl(n)
        # print(c, len(str(c).replace('0', '')))
        l = len(str(c).replace('0', ''))
        if l not in [3, 4, 5]:
            # print(c, len(str(c).replace('0', '')))
            continue
        num += 1
        for i in range(8):
            if c[i] == "1":
                print('Кликаю', c, i + 1)
                click(f'div[data-state="no_submission"]>:nth-child({i + 1}) span[class ="s-checkbox__circle"]')
                time.sleep(0.1)

        click(".submit-submission")
        # print('Отправляю')
        time.sleep(1.5)
        try:
            if "Вы получили" in browser.find_element_by_css_selector(".attempt__score-info").text:
                print()
                print('Готово! C', num, 'попытки. Вариантов ответа', l, '\nОтветы:')
                print(c)
                return
        except Exception:
            pass
        click(".again-btn")
        # print('Пробую еще')
        time.sleep(3)
        if n > 255:
            return print("!")


def ss():
    browser.get("https://stepik.org/lesson/9531/step/11?unit=1792")
    time.sleep(4)
    browser.execute_script("window.scrollBy(0, 300);")
    c()


ss()
