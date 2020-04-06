import pytest
from selenium import webdriver


def test_add_to_basket_button(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    try:
        browser.find_element_by_css_selector('.btn-add-to-basket')
    except Exception:
        raise AssertionError('Element was not found')
