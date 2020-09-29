from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    func = math.log(abs(12*math.sin(x)))
    print(x)
    print(func)
    input_et = browser.find_element_by_id('answer').send_keys(str(func))

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
