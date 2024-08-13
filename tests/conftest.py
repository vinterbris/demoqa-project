import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://demoqa.com/text-box'
    browser.config.timeout = 2.0
    browser.config.window_width = 1900
    browser.config.window_height = 1000

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


    yield

    browser.quit()