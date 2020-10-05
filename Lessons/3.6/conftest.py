import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nЗапускаю Chrome для теста..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nЗапускаю Firefox для теста..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nБраузер не задан, запускаю Chrome..")
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
