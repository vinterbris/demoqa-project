from selene import browser, command, have


def test_text_box():
    name = 'Ellend Venture'
    email = 'ellend@venture.com'
    address = 'Keep Venture, Luthadel'

    browser.open('/')

    # WHEN
    browser.element('#userName').type(name)
    browser.element('#userEmail').type(email)
    browser.element('#currentAddress').type(address)
    browser.element('#permanentAddress').type(address)
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # THEN
    browser.all('#output>div>p').should(
        have.texts(
            f'Name:{name}',
            f'Email:{email}',
            f'Current Address :{address}',
            f'Permananet Address :{address}'
        )
    )
