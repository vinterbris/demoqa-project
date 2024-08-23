import allure

from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import student


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Регистрация")
@allure.story("Короткая регистрация")
def test_successful_simple_user_registration():
    app.side_panel.open_simple_registration_form()

    # WHEN
    app.simple_registration_page.fill_form(student)
    app.simple_registration_page.submit_form()

    # THEN
    app.simple_registration_page.should_have_registered_user_data(student)


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Регистрация")
@allure.story("Полная регистрация")
def test_successful_user_registration():
    app.side_panel.open_registration_form()

    # WHEN
    app.registration_page.fill_form(student)
    app.registration_page.submit_form()

    # THEN
    app.registration_page.should_have_registered_user_data(student)
    app.registration_page.close_modal_window()


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Radio button")
def test_radio_button_yes():
    app.side_panel.open_radio_button_page()

    app.radio_button_page.click_yes()

    app.radio_button_page.should_have_text('Yes')


def test_check_notes():
    app.side_panel.open_check_box_page()

    # WHEN
    app.check_box_page.toggle_home()
    app.check_box_page.toggle_desktop()
    app.check_box_page.choose_notes()

    # THEN
    app.check_box_page.should_be_half_checked('Home')
    app.check_box_page.should_be_half_checked('Desktop')
    app.check_box_page.should_be_checked('Notes')
    app.check_box_page.should_have_selections('notes')


# def test_check_home():
#     app.side_panel.open_check_box_page()
#
#     app.check_box_page.choose_home()
#
#     app.check_box_page.
