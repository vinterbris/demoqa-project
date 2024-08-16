from selene import browser, command, have

from demoqa_ui_tests import resources
from demoqa_ui_tests.models.pages.simple_student_registration_page import (
    SimpleRegistrationPage,
)
from demoqa_ui_tests.test_data.users import student


class RegistrationPage:

    def __init__(self): ...


def test_successful_simple_user_registration():
    registration_page = SimpleRegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill(student)
    registration_page.submit_form()

    # THEN
    registration_page.should_have_registered_user_data(student)


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

    browser.element('#currentAddress').type(current_address)

    browser.element('#react-select-3-input').type(state).press_enter()
    browser.element('#react-select-4-input').type(city).press_enter()

    browser.element('#submit').click()

    # THEN
    browser.element('.modal-content').element('.table').all('td:last-child').should(
        have.exact_texts(
            f'{name} {last_name}',
            email,
            gender,
            phone_number,
            date_of_birth,
            f'{study_subject1}, {study_subject2}',
            hobbies,
            img_name,
            current_address,
            f'{state} {city}',
        )
    )
    browser.element('#closeLargeModal').with_(click_by_js=True)
