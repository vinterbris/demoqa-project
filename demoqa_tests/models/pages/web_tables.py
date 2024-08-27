from selene import browser, have
from selene.support.conditions import be

from demoqa_tests.plugins.allure.report import step


class WebTables:

    @step
    def delete_person(self, first_name):
        browser.all('.rt-td').element_by(have.exact_text(first_name)).element(
            '..'
        ).element('#delete-record-1').click()

    @step
    def should_be_deleted(self, first_name):
        browser.all('.rt-td').element_by(have.exact_text(first_name)).should(be.absent)

    @step
    def find_person(self, first_name):
        browser.element('#searchBox').click().type(first_name)

    @step
    def add_person(self, worker):
        browser.element('#addNewRecordButton').click()
        browser.element('#firstName').type(worker.fist_name)
        browser.element('#lastName').type(worker.last_name)
        browser.element('#userEmail').type(worker.email)
        browser.element('#age').type(worker.age)
        browser.element('#salary').type(worker.salary)
        browser.element('#department').type(worker.department)
        browser.element('#submit').click()

    @step
    def edit_person(self, worker):
        browser.element('#edit-record-1').click()
        browser.element('#firstName').set_value(worker.fist_name)
        browser.element('#lastName').set_value(worker.last_name)
        browser.element('#userEmail').set_value(worker.email)
        browser.element('#age').set_value(worker.age)
        browser.element('#salary').set_value(worker.salary)
        browser.element('#department').set_value(worker.department)
        browser.element('#submit').click()

    @step
    def should_be_found(self, first_name):
        browser.all('.rt-td').element_by(have.exact_text(first_name)).should(be.present)

    @step
    def other_rows_should_have_no_peope(self, *names):
        browser.all('.rt-tr-group .rt-td:first-child').element_by(
            have.exact_texts(*names)
        ).should(be.absent)

    @step
    def should_exist(self, worker):
        self.find_person(worker.fist_name)
        browser.all('.rt-tr-group').first.all('.rt-td').should(
            have.exact_texts(
                worker.fist_name,
                worker.last_name,
                worker.age,
                worker.email,
                worker.salary,
                worker.department,
                '',
            )
        )
