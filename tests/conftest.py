from pathlib import Path

import pytest
from selene import browser
from selenium import webdriver

user_data = Path().home() / 'my home profile'
profile_dir = 'Default'


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1600
    browser.config.window_height = 900

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    # driver_options.add_argument('--headless=new')
    driver_options.add_argument(f'user-data-dir={user_data}')
    driver_options.add_argument(f'profile-directory={profile_dir}')
    browser.config.driver_options = driver_options

    yield

    browser.quit()
