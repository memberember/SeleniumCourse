from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    func = math.log(abs(12*math.sin(x)))
    print(x)
    print(func)
    input_et = browser.find_element_by_id('answer').send_keys(str(func))

    cb_robot = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", cb_robot)

    cb_robot.click()

    rb_robot = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb_robot)
    rb_robot.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
