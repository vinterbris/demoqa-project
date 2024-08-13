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
    browser.element('#name').should(have.text(f'Name:{name}'))
    browser.element('#email').should(have.text(f'Email:{email}'))
    # browser.element('#currentAddress').should(have.text(f'Current Address :{address}'))
    # browser.element('#permanentAddress').should(have.text(f'Permananet Address :{address}'))

    # browser.all('#output>p').should(have.texts(f'Name:{name}', f'Email:{email}'))
