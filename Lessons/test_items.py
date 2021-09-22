import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_i_should_see_basket(browser):
    browser.get(link)
    time.sleep(3)
    basket = browser.find_elements_by_css_selector('button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert len(basket) != 0, 'there is no basket here'
