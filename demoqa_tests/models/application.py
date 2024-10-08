from demoqa_tests.models.components.side_panel import SidePanel
from demoqa_tests.models.pages.check_box_page import CheckBox
from demoqa_tests.models.pages.main_page import MainPage
from demoqa_tests.models.pages.radio_button_page import RadioButtonPage
from demoqa_tests.models.pages.simple_student_registration_page import (
    SimpleRegistrationPage,
)
from demoqa_tests.models.pages.student_registration_page import RegistrationPage
from demoqa_tests.models.pages.web_tables import WebTables


class Application:

    def __init__(self):
        self.main_page = MainPage()
        self.side_panel = SidePanel()
        self.simple_registration_page = SimpleRegistrationPage()
        self.registration_page = RegistrationPage()
        self.radio_button_page = RadioButtonPage()
        self.check_box_page = CheckBox()
        self.web_tables = WebTables()


app = Application()
