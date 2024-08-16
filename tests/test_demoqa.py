from demoqa_ui_tests.models.pages.simple_student_registration_page import (
    SimpleRegistrationPage,
)
from demoqa_ui_tests.models.pages.student_registration_page import RegistrationPage
from demoqa_ui_tests.test_data.users import student


def test_successful_simple_user_registration():
    registration_page = SimpleRegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_form(student)
    registration_page.submit_form()

    # THEN
    registration_page.should_have_registered_user_data(student)


def test_successful_user_registration():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_form(student)
    registration_page.submit_form()

    # THEN
    registration_page.should_have_registered_user_data(student)
    registration_page.close_modal_window()
