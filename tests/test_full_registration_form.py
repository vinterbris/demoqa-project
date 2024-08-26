import allure
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import student


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
