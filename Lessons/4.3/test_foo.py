from pages.product_page import ProductPage
import pytest

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   # pytest.param(
#                                   #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   #     marks=pytest.mark.xfail(reason='Неправильное название в корзине')),
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     title = page.get_product_title()
#     price = page.get_product_price()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     assert title == page.get_title_product_title(), f'Названия продуктов по ссылке {link} не совпадают'
#     assert price == page.get_title_product_price(), f'Цены продуктов по ссылке {link} не совпадает'


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.is_success_message_disappeared()
