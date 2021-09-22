## Финальное задание курса "Автоматизация тестирования с помощью Selenium и Python"
https://stepik.org/course/575/

##### Пометка проверяющим:
##### 1) Если появляются ошибки связанные с имортом:

from .pages.basket_page import BasketPage\
ImportError: attempted relative import with no known parent package

Удалите точки пред pages:

В файле test_product_page.py:

from .pages.basket_page import BasketPage\
from .pages.product_page import ProductPage\
from .pages.login_page import LoginPage

В файле test_main_page.py:

from .pages.main_page import MainPage\
from .pages.login_page import LoginPage\
from .pages.basket_page import BasketPage

##### 2) Если такая ошибка:
ValueError: option names {'--browser_name'} already added

У вас есть, например, в верхнем каталоге, дубликат файла conftest.py
