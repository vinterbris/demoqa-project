from selene import browser, have, command

from demoqa_ui_tests.models.components.side_panel import SidePanel
from demoqa_ui_tests.models.pages.main_page import MainPage
from demoqa_ui_tests.models.pages.simple_student_registration_page import (
    SimpleRegistrationPage,
)
from demoqa_ui_tests.models.pages.student_registration_page import RegistrationPage


class Application:

    def __init__(self):
        self.main_page = MainPage()
        self.side_panel = SidePanel()
        self.simple_registration_page = SimpleRegistrationPage()
        self.registration_page = RegistrationPage()


app = Application()
