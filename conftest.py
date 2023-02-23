import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Разобраться как работает выбор языка. Добавить выбор 4-х языков. Предусмотреть выбор браузера.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: now available en, cn, ru, uz")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1920, 1080)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
        browser.set_window_size(1920, 1080)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
