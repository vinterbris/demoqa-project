from selene import browser, have
from selene.support.conditions import be

from demoqa_ui_tests.plugins.allure.report import step


class CheckBox:

    @step
    def toggle_home(self):
        browser.element('[for="tree-node-home"]').element('..').element('button').click()

    @step
    def toggle_desktop(self):
        browser.element('[for="tree-node-desktop"]').element('..').element(
            'button'
        ).click()

    @step
    def check_notes(self):
        browser.element('#tree-node-notes').click()

    @step
    def expand_list(self):
        browser.element('[title="Expand all"]').click()

    @step
    def collapse_list(self):
        browser.element('[title="Collapse all"]').click()

    @step
    def choose_home(self):
        browser.element('#tree-node-home').click()

    @step
    def choose_notes(self):
        # self.expand_all.click()
        browser.all('.rct-title').element_by(have.text('Notes')).click()

    @step
    def should_be_checked(self, value):
        browser.all('.rct-text').element_by(have.text(value)).element(
            '.rct-icon-check'
        ).matching(be.present)

    @step
    def should_be_half_checked(self, value):
        browser.all('.rct-text').element_by(have.text(value)).element(
            '.rct-icon-half-check'
        ).matching(be.present)

    @step
    def should_have_selections(self, *checkboxes):
        browser.element('#result').should(have.text(*checkboxes))
