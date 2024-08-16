from selene import browser, have, command


class MainPage:

    def open_elements(self):
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text('Elements')).click()

    def open_forms(self):
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text('Forms')).click()

    def open_alerts(self):
        browser.open('/')
        browser.all('.card-body').element_by(
            have.exact_text('Alerts, Frame & Windows')
        ).click()

    def open_widgets(self):
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text('Widgets')).click()

    def open_interactions(self):
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text('Interactions')).click()

    def open_book_store_application(self):
        browser.open('/')
        browser.all('.card-body').element_by(
            have.exact_text('Book Store Application')
        ).perform(command.js.scroll_into_view).click()
