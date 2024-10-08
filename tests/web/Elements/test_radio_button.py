import allure
from allure_commons.types import Severity

from demoqa_tests.models.application import app


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Элементы")
@allure.feature("Radio button")
@allure.story("Включение")
def test_radio_button_yes():
    app.side_panel.open_radio_button_page()

    app.radio_button_page.click_yes()

    app.radio_button_page.should_have_text('Yes')


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Элементы")
@allure.feature("Radio button")
@allure.story("Переключение")
def test_radio_button_switch():
    app.side_panel.open_radio_button_page()

    app.radio_button_page.click_yes()
    app.radio_button_page.click_impressive()

    app.radio_button_page.should_have_text('Impressive')
    app.radio_button_page.button_no_should_not_be_available()
