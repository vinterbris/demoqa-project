import allure
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Удаление")
def test_delete_person():
    app.side_panel.open_web_tables_form()

    app.web_tables.delete_person(first_name='Cierra')

    app.web_tables.should_be_deleted(first_name='Cierra')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Поиск")
def test_search_person():
    app.side_panel.open_web_tables_form()


# search
# add
# edit
