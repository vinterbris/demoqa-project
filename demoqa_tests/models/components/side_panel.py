from selene import browser, have

from demoqa_tests.models.pages.main_page import MainPage
from demoqa_tests.plugins.allure.report import step


class SidePanel:

    def __init__(self):
        self.main_page = MainPage()
        self.header_name = browser.all('.header-text')

    def _open(self, element_group, item):
        self.main_page.open(element_group)
        browser.all('.text').element_by(have.exact_text(item)).click()

    @step
    def open_simple_registration_form(self):
        self._open('Elements', 'Text Box')

    @step
    def open_radio_button_page(self):
        self._open('Elements', 'Radio Button')

    @step
    def open_check_box_page(self):
        self._open('Elements', 'Check Box')

    @step
    def open_registration_form(self):
        self._open('Forms', 'Practice Form')

    @step
    def open_web_tables_form(self):
        self._open('Elements', 'Web Tables')
