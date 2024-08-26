import allure
from allure_commons.types import Severity

from demoqa_ui_tests.models.application import app


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
    app.check_box_page.click_checkbox('Notes')

    # THEN
    app.check_box_page.should_be_half_checked('Home')
    app.check_box_page.should_be_half_checked('Desktop')
    app.check_box_page.should_be_checked('Notes')
    app.check_box_page.should_have_selections('notes')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Check box")
def test_check_home():
    app.side_panel.open_check_box_page()

    app.check_box_page.click_checkbox('Home')

    app.check_box_page.expand_list()
    app.check_box_page.should_be_ckecked_amount_of_items(17)
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
@allure.severity(Severity.NORMAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Элементы")
@allure.story("Check box")
def test_uncheck_all():
    app.side_panel.open_check_box_page()

    app.check_box_page.expand_list()
    app.check_box_page.click_checkbox('Home')
    app.check_box_page.click_checkbox('Home')

    app.check_box_page.should_be_ckecked_amount_of_items(0)
    app.check_box_page.should_not_have_selections()
