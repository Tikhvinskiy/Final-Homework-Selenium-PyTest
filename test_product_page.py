import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_button()
    page.solve_quiz_and_get_code()
    page.check_product_name_and_adding()
    page.check_message_basket_total()
