import allure
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import simple_student


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Регистрация")
@allure.story("Короткая регистрация")
def test_successful_simple_user_registration():
    app.side_panel.open_simple_registration_form()

    # WHEN
    app.simple_registration_page.fill_form(simple_student)
    app.simple_registration_page.submit_form()

    # THEN
    app.simple_registration_page.should_have_registered_user_data(simple_student)
