from pathlib import Path

import allure_commons
import pytest
from selene import browser, support, Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import project
from demoqa_ui_tests.utils import attach

CHROME_PROFILE_WITH_UBLOCK = Path().home()
PROFILE_DIR = 'Default'


@pytest.fixture(scope='session', autouse=True)
def add_reporting_to_selene_steps():
    '''
    Code from https://github.com/yashaka/python-web-test
    :return:
    '''

    from demoqa_ui_tests.plugins.python import monkey

    original_open = Browser.open

    @monkey.patch_method_in(Browser)
    def open(self, relative_or_absolute_url: str):
        from demoqa_ui_tests.plugins.allure import report

        return report.step(original_open)(self, relative_or_absolute_url)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    selenoid = project.config.selenoid
    browser_version = project.config.browser_version
    selenoid_url = project.config.selenoid_url + '/wd/hub'
    selenoid_ui_url = project.config.selenoid_ui_url

    browser.config.base_url = project.config.base_url
    browser.config.timeout = project.config.timeout
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height

    options = Options()
    options.page_load_strategy = 'eager'
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    if selenoid:
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        selenoid_capabilities = {
            "browserName": 'chrome',
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(command_executor=selenoid_url, options=options)

        browser.config.driver = driver
    else:
        options.add_argument(f'user-data-dir={CHROME_PROFILE_WITH_UBLOCK}')
        options.add_argument(f'profile-directory={PROFILE_DIR}')
        browser.config.driver_options = options

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_ui_url)

    browser.quit()
