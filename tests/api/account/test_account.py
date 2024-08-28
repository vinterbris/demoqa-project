import allure
from allure_commons.types import Severity

from demoqa_tests.test_data.api_users import valid_credentials, invalid_credentials
from demoqa_tests.utils.http_logger import send_request


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Аккаунт")
@allure.feature("Авторизация")
@allure.story("Успешная")
def test_successful_authorization():
    data = valid_credentials

    response = send_request('/Account/v1/Authorized', 'post', json=data)
    body = response.json()

    assert response.status_code == 200
    assert body == True


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Аккаунт")
@allure.feature("Авторизация")
@allure.story("Проваленная")
def test_failed_authorization():
    data = invalid_credentials

    response = send_request('/Account/v1/Authorized', 'post', json=data)
    body = response.json()

    assert response.status_code == 404
    assert body['code'] == '1207'
    assert body['message'] == 'User not found!'


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Аккаунт")
@allure.feature("Авторизация")
@allure.story("Без данных для входа")
def test_authorization_without_credentials():

    response = send_request('/Account/v1/Authorized', 'post')
    body = response.json()

    assert response.status_code == 400
    assert body['code'] == '1200'
    assert body['message'] == 'UserName and Password required.'


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Аккаунт")
@allure.feature("Генерация токена")
@allure.story("Успешная")
def test_successful_token_generation():
    data = valid_credentials

    response = send_request('/Account/v1/GenerateToken', 'post', json=data)
    body = response.json()

    assert response.status_code == 200
    assert body.get('token') is not None
    assert body.get('expires') is not None
    assert body['status'] == 'Success'
    assert body['result'] == 'User authorized successfully.'


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.epic("Аккаунт")
@allure.feature("Генерация токена")
@allure.story("Проваленная")
def test_failed_token_generation():
    data = invalid_credentials

    response = send_request('/Account/v1/GenerateToken', 'post', json=data)
    body = response.json()

    assert response.status_code == 200
    assert body.get('token') is None
    assert body.get('expires') is None
    assert body['status'] == 'Failed'
    assert body['result'] == 'User authorization failed.'
