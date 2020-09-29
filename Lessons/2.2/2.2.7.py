from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os


try:
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Ivan')

    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Petrov')

    email = browser.find_element_by_name('email')
    email.send_keys('kot@aawe.df')

    file_btn = browser.find_element_by_css_selector('[type="file"]')
    file_btn.send_keys(file_path)

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
