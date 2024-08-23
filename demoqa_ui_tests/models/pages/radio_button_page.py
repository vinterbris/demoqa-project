from selene import browser, have

from demoqa_ui_tests.plugins.allure.report import step


class RadioButtonPage:

    @step
    def click_yes(self):
        browser.element('[for="yesRadio"]').click()

    @step
    def click_impressive(self):
        browser.element('[for="impressiveRadio"]').click()

    @step
    def should_have_text(self, value):
        browser.element('.text-success').should(have.exact_text(value))
