from selene import browser, command, have


class SimpleRegistrationPage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.button_submit = browser.element('#submit')
        self.table = browser.all('#output p')

    def open(self):
        browser.open('/text-box')

    def _enter_full_name(self, value):
        self.full_name.type(value)

    def _enter_email(self, value):
        self.email.type(value)

    def _enter_current_address(self, value):
        self.current_address.type(value)

    def _enter_permanent_address(self, value):
        self.permanent_address.type(value)

    def submit_form(self):
        self.button_submit.perform(command.js.scroll_into_view).click()

    def should_have_registered_user_data(self, student):
        self.table.should(
            have.texts(
                f'Name:{student.full_name}',
                f'Email:{student.email}',
                f'Current Address :{student.current_address}',
                f'Permananet Address :{student.permanent_address}',
            )
        )

    def fill(self, student):
        self._enter_full_name(student.full_name)
        self._enter_email(student.email)
        self._enter_current_address(student.current_address)
        self._enter_permanent_address(student.permanent_address)
