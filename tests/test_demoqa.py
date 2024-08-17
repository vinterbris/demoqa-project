import allure
from allure_commons._allure import step
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.users import student


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Регистрация")
@allure.story("Короткая регистрация")
def test_successful_simple_user_registration():
    with step('Открываем форму простой регистрации'):
        app.side_panel.open_simple_registration_form()

    # WHEN
    with step('Заполняем форму'):
        app.simple_registration_page.fill_form(student)
    with step('Отправляем форму'):
        app.simple_registration_page.submit_form()

    # THEN
    with step('Проверяем данные зарегистрированного пользоателя'):
        app.simple_registration_page.should_have_registered_user_data(student)


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Регистрация")
@allure.story("Полная регистрация")
def test_successful_user_registration():
    with step('Открываем форму простой регистрации'):
        app.side_panel.open_registration_form()

    # WHEN
    with step('Заполняем форму'):
        app.registration_page.fill_form(student)
    with step('Отправляем форму'):
        app.registration_page.submit_form()

    # THEN
    with step('Проверяем данные зарегистрированного пользоателя'):
        app.registration_page.should_have_registered_user_data(student)
    with step('Закрываем модальное окно'):
        app.registration_page.close_modal_window()
