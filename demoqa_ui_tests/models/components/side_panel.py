from selene import browser, have


class SidePanel:

    def _open(self, element_group, menu_item):
        current_element_group = browser.all('.element-group').element_by(
            have.exact_text(element_group)
        )
        current_element_group.click()
        current_element_group.all()

    def open_simple_registration_form(self): ...

    def open_registration_form(self): ...
