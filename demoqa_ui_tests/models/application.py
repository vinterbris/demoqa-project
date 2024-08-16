from demoqa_ui_tests.models.pages.simple_student_registration_page import (
    SimpleRegistrationPage,
)
from demoqa_ui_tests.models.pages.student_registration_page import RegistrationPage


class Application:

    def __init__(self):
        self.simple_registration_page = SimpleRegistrationPage()
        self.registration_page = RegistrationPage()


app = Application()
