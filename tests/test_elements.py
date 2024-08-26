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
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Check box")
def test_check_notes():
    app.side_panel.open_check_box_page()

    # WHEN
    app.check_box_page.toggle_home()
    app.check_box_page.toggle_desktop()
    app.check_box_page.choose_checkbox('Notes')

    # THEN
    app.check_box_page.should_be_half_checked('Home')
    app.check_box_page.should_be_half_checked('Desktop')
    app.check_box_page.should_be_checked('Notes')
    app.check_box_page.should_have_selections('notes')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Radio button")
def test_check_home():
    app.side_panel.open_check_box_page()

    app.check_box_page.choose_checkbox('Home')

    app.check_box_page.expand_list()
    app.check_box_page.should_all_be_ckecked()
    app.check_box_page.should_have_selections(
        'home',
        'desktop',
        'notes',
        'commands',
        'documents',
        'workspace',
        'react',
        'angular',
        'veu',
        'office',
        'public',
        'private',
        'classified',
        'general',
        'downloads',
        'wordFile',
        'excelFile',
    )


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Radio button")
def test_radio_button_yes():
    app.side_panel.open_radio_button_page()

    app.radio_button_page.click_yes()

    app.radio_button_page.should_have_text('Yes')
