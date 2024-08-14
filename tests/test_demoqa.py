import os

from selene import browser, command, have
from selenium.webdriver import Keys

import tests
from demoqa_tests.test_data.data import full_name, email, address

CURRENT_FILE = os.path.abspath(tests.__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
RES_DIR = os.path.join(CURRENT_DIR, os.path.pardir, "resources/images")


def test_text_box():
    browser.open('/text-box')

    # WHEN
    browser.element('#userName').type(full_name)
    browser.element('#userEmail').type(email)
    browser.element('#currentAddress').type(address)
    browser.element('#permanentAddress').type(address)
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # THEN
    browser.all('#output>div>p').should(
        have.texts(
            f'Name:{full_name}',
            f'Email:{email}',
            f'Current Address :{address}',
            f'Permananet Address :{address}',
        )
    )


def test_practice_form():
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

    browser.element("#uploadPicture").set_value(
        os.path.abspath(os.path.join(RES_DIR, img_name))
    )

    browser.element('#currentAddress').type(address)

    browser.element('#react-select-3-input').type(state).press_enter()
    browser.element('#react-select-4-input').type(city).press_enter()

    browser.element('#submit').click()

    # THEN
    browser.element('.table').all('td:last-child').should(
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
