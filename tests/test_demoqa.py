from selene import browser, have

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import student


def test_successful_simple_user_registration():
    app.simple_registration_page.open()

    # WHEN
    app.simple_registration_page.fill_form(student)
    app.simple_registration_page.submit_form()

    # THEN
    app.simple_registration_page.should_have_registered_user_data(student)


def test_successful_user_registration():
    app.registration_page.open()

    # WHEN
    app.registration_page.fill_form(student)
    app.registration_page.submit_form()

    # THEN
    app.registration_page.should_have_registered_user_data(student)
    app.registration_page.close_modal_window()


def test():
    browser.open('/')
    element_group = 'Elements'
    menu_item = ''

    current_element_group = browser.all('.header-text').element_by(
        have.exact_text(element_group)
    )
    current_element_group.click()
    # current_element_group.all()


def test_main_page():
    app.main_page.open_book_store_application()
