from selene import browser, have
from selene.support.conditions import be

from demoqa_ui_tests.plugins.allure.report import step


class WebTables:

    @step
    def delete_person(self, first_name):
        browser.all('.rt-td').element_by(have.exact_text(first_name)).element(
            '..'
        ).element('#delete-record-1').click()

    @step
    def should_be_deleted(self, first_name):
        browser.all('.rt-td').element_by(have.exact_text(first_name)).should(be.absent)
