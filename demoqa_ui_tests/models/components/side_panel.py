from selene import browser, have, be

from demoqa_ui_tests.models.pages.main_page import MainPage


class SidePanel:

    def __init__(self):
        self.main_page = MainPage()
        self.header_name = browser.all('.header-text')

    def _open(self, element_group, item):

        self.main_page.open(element_group)
        browser.all('.text').element_by(have.exact_text(item)).click()

    def open_simple_registration_form(self):
        self._open('Elements', 'Text Box')

    def open_registration_form(self):
        self._open('Forms', 'Practice Form')
