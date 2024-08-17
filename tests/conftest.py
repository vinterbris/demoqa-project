from pathlib import Path

import pytest
from selene import browser
from selenium import webdriver

from demoqa_ui_tests.utils import attach

from config import Config

config = Config()

CHROME_PROFILE_WITH_UBLOCK = Path().home()
PROFILE_DIR = 'Default'


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='124.0')
    parser.addoption('--selenoid', default=False)
    parser.addoption('--selenoid_url', default='http://localhost:4444')
    parser.addoption('--selenoid_ui_url', default='http://localhost:8080')


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    run_selenoid = request.config.getoption('--selenoid')
    selenoid_url = request.config.getoption('--selenoid_url')
    selenoid_ui_url = request.config.getoption('--selenoid_ui_url')

    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument(f'user-data-dir={CHROME_PROFILE_WITH_UBLOCK}')
    driver_options.add_argument(f'profile-directory={PROFILE_DIR}')
    browser.config.driver_options = driver_options

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    # attach.add_video(browser, selenoid_ui_url)

    browser.quit()
