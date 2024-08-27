import allure
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app
from demoqa_ui_tests.test_data.names import name, names
from demoqa_ui_tests.test_data.users import worker


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Удаление")
def test_delete_person():
    app.side_panel.open_web_tables_form()

    app.web_tables.delete_person(first_name=name)

    app.web_tables.should_be_deleted(first_name=name)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Поиск")
def test_search_person():
    app.side_panel.open_web_tables_form()

    app.web_tables.find_person(first_name=name)

    app.web_tables.should_be_found(first_name=name)
    app.web_tables.other_rows_should_have_no_peope(names)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Добавление")
def test_add_person():
    app.side_panel.open_web_tables_form()

    app.web_tables.add_person(worker)

    app.web_tables.should_exist(worker)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Таблица")
@allure.story("Редактирование")
def test_edit_person():
    app.side_panel.open_web_tables_form()

    app.web_tables.edit_person(worker)

    app.web_tables.should_exist(worker)
