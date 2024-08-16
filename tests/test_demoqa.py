from selene import browser, have

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import student


def test_successful_simple_user_registration():
    app.side_panel.open_simple_registration_form()

    # WHEN
    app.simple_registration_page.fill_form(student)
    app.simple_registration_page.submit_form()

    # THEN
    app.simple_registration_page.should_have_registered_user_data(student)


def test_successful_user_registration():
    app.side_panel.open_registration_form()

    # WHEN
    app.registration_page.fill_form(student)
    app.registration_page.submit_form()

    # THEN
    app.registration_page.should_have_registered_user_data(student)
    app.registration_page.close_modal_window()
