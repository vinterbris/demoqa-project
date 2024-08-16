from selene import browser, command, have

from demoqa_ui_tests import resources
from demoqa_ui_tests.test_data.data import full_name, email, address


class SimpleRegistrationPage:

    def __init__(self): ...

    def open(self):
        browser.open('/text-box')

    def enter_full_name(self, value):
        browser.element('#userName').type(value)

    def enter_email(self, value):
        browser.element('#userEmail').type(value)

    def enter_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def enter_permanent_address(self, value):
        browser.element('#permanentAddress').type(value)

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()


class RegistrationPage:

    def __init__(self): ...


def test_successful_simple_user_registration():
    simple_registration_page = SimpleRegistrationPage()

    simple_registration_page.open()

    # WHEN
    simple_registration_page.enter_full_name(full_name)
    simple_registration_page.enter_email(email)
    simple_registration_page.enter_current_address(address)
    simple_registration_page.enter_permanent_address(address)
    simple_registration_page.submit_form()

    # THEN
    browser.all('#output p').should(
        have.texts(
            f'Name:{full_name}',
            f'Email:{email}',
            f'Current Address :{address}',
            f'Permananet Address :{address}',
        )
    )


def test_successful_user_registration():
    name = 'Ellend'
    last_name = 'Venture'
    gender = 'Male'
    phone_number = '9998887755'
    day_of_birth = '15'
    month_of_birth = 'November'
    year_of_birth = '1900'
    date_of_birth = day_of_birth + ' ' + month_of_birth + ',' + year_of_birth
    study_subject1 = 'Physics'
    study_subject2 = 'Maths'
    hobbies = 'Sports, Reading, Music'
    img_name = 'tom-byrom.jpg'
    state = 'NCR'
    city = 'Delhi'

    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
    browser.element('#userNumber').type(phone_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type(year_of_birth)
    browser.element('.react-datepicker__month-select').type(month_of_birth)
    browser.element(f'.react-datepicker__day--0{day_of_birth}').click()

    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type(study_subject1).press_enter()
    browser.element('#subjectsInput').type(study_subject2).press_enter()

    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Reading')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()

    browser.element('#submit').perform(command.js.scroll_into_view)

    browser.element("#uploadPicture").set_value(resources.path(img_name))

    browser.element('#currentAddress').type(address)

    browser.element('#react-select-3-input').type(state).press_enter()
    browser.element('#react-select-4-input').type(city).press_enter()

    browser.element('#submit').click()

    # THEN
    browser.element('.modal-content').element('.table').all('td:last-child').should(
        have.exact_texts(
            ' '.join([name, last_name]),
            email,
            gender,
            phone_number,
            date_of_birth,
            ', '.join([study_subject1, study_subject2]),
            hobbies,
            img_name,
            address,
            ' '.join([state, city]),
        )
    )
    browser.element('#closeLargeModal').with_(click_by_js=True)
