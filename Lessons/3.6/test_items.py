import time

link = "http://selenium1py.pythonanywhere.com/catalogu/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    assert browser.find_element_by_class_name('btn-add-to-basket'), "Кнопка не найдена!"
    time.sleep(4)
