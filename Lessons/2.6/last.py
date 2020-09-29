import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет 100
    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_id("book")
    button.click()

    x = int(browser.find_element_by_id('input_value').text)
    func = math.log(abs(12 * math.sin(x)))
    print(x)
    print(func)
    input_et = browser.find_element_by_id('answer').send_keys(str(func))

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
