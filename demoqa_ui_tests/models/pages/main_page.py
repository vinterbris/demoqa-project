from selene import browser, have, command


class MainPage:

    def open(self, card_name):
        '''
        Recieves: Elements/Forms/Alerts, Frame & Windows/Widgets/Interactions/Book Store Application
        '''
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text(card_name)).perform(
            command.js.scroll_into_view
        ).click()
