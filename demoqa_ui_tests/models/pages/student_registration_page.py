from selene import browser, have, command

from demoqa_ui_tests import resources


class RegistrationPage:

    def __init__(self):
        self.button_submit = browser.element('#submit')
        self.checkboxes_hobbies = browser.all('[for^=hobbies-checkbox]')
        self.field_subjects = browser.element('#subjectsInput')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_form(self, student):
        self.enter_name(student)
        self._enter_last_name(student)
        self._enter_email(student)
        self.pick_gender(student)
        self._enter_phone_number(student)

        self.enter_birth_date(student)
        self.enter_subjects(student)
        self.enter_hobbies(student)

        self.scroll_to_the_submit_button()

        self.upload_picture(student)
        self.enter_current_address(student)
        self.pick_state_and_city(student)

    def enter_name(self, student):
        browser.element('#firstName').type(student.name)

    def _enter_last_name(self, student):
        browser.element('#lastName').type(student.last_name)

    def _enter_email(self, student):
        browser.element('#userEmail').type(student.email)

    def pick_gender(self, student):
        browser.all('[name=gender]').element_by(have.value(student.gender)).element(
            '..'
        ).click()

    def _enter_phone_number(self, student):
        browser.element('#userNumber').type(student.phone_number)

    def enter_birth_date(self, student):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(student.year_of_birth)
        browser.element('.react-datepicker__month-select').type(student.month_of_birth)
        browser.element(f'.react-datepicker__day--0{student.day_of_birth}').click()

    def enter_subjects(self, student):
        browser.element('#subjectsContainer').click()
        self.field_subjects.type(student.study_subject1).press_enter()
        self.field_subjects.type(student.study_subject2).press_enter()

    def enter_hobbies(self, student):
        self.checkboxes_hobbies.element_by(have.text('Sports')).click()
        self.checkboxes_hobbies.element_by(have.text('Reading')).click()
        self.checkboxes_hobbies.element_by(have.text('Music')).click()

    def scroll_to_the_submit_button(self):
        self.button_submit.perform(command.js.scroll_into_view)

    def enter_current_address(self, student):
        browser.element('#currentAddress').type(student.current_address)

    def pick_state_and_city(self, student):
        browser.element('#react-select-3-input').type(student.state).press_enter()
        browser.element('#react-select-4-input').type(student.city).press_enter()

    def submit_form(self):
        self.button_submit.click()

    def should_have_registered_user_data(self, student):
        browser.element('.modal-content').element('.table').all('td:last-child').should(
            have.exact_texts(
                f'{student.name} {student.last_name}',
                student.email,
                student.gender,
                student.phone_number,
                f'{student.day_of_birth} {student.month_of_birth},{student.year_of_birth}',
                f'{student.study_subject1}, {student.study_subject2}',
                student.hobbies,
                student.img_name,
                student.current_address,
                f'{student.state} {student.city}',
            )
        )

    def close_modal_window(self):
        browser.element('#closeLargeModal').with_(click_by_js=True)

    def upload_picture(self, student):
        browser.element("#uploadPicture").set_value(resources.path(student.img_name))
