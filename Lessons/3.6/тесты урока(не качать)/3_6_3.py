import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1'
    , 'https://stepik.org/lesson/236896/step/1'
    , 'https://stepik.org/lesson/236897/step/1'
    , 'https://stepik.org/lesson/236898/step/1'
    , 'https://stepik.org/lesson/236899/step/1'
    , 'https://stepik.org/lesson/236903/step/1'
    , 'https://stepik.org/lesson/236904/step/1'
    , 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    # говорим Selenium проверять в течение 10 секунд, пока поле текста не появится
    textfield = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
    )
    answer = math.log(int(time.time()))
    textfield.send_keys(str(answer))
    button = browser.find_element_by_class_name('submit-submission')
    button.click()

    message = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    )
    assert "Correct!" in message.text, 'Ошибка ожидалось {}, в тесте {}'.format("Correct!", message.text)




