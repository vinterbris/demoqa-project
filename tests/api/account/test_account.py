import allure
from allure_commons.types import Severity
from faker import Faker

import project
from demoqa_tests.test_data.api_users import valid_credentials
from demoqa_tests.utils.http_logger import send_request

fake = Faker()


class TestAuthorization:
    @allure.tag("api")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "dobrovolskiysv")
    @allure.epic("Аккаунт")
    @allure.feature("Авторизация")
    @allure.story("Успешная")
    def test_successful_authorization(self):
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
    @allure.story("С неправильным паролем")
    def test_authorization_with_wrong_password(self):
        data = {"userName": project.config.login, "password": fake.password()}

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
    @allure.story("С неправильным логином")
    def test_authorization_with_wrong_login(self):
        data = {"userName": fake.email(), "password": fake.password()}

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
    @allure.story("С пустым паролем")
    def test_authorization_with_empty_password(self):
        data = {"userName": project.config.login, "password": fake.password()}

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
    @allure.story("С пустым логином")
    def test_authorization_with_empty_login(self):
        data = {"userName": project.config.login, "password": ''}

        response = send_request('/Account/v1/Authorized', 'post', json=data)
        body = response.json()

        assert response.status_code == 400
        assert body['code'] == '1200'
        assert body['message'] == 'UserName and Password required.'

    @allure.tag("api")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "dobrovolskiysv")
    @allure.epic("Аккаунт")
    @allure.feature("Авторизация")
    @allure.story("Без данных для входа")
    def test_authorization_with_empty_body(self):
        data = {}

        response = send_request('/Account/v1/Authorized', 'post', json=data)
        body = response.json()

        assert response.status_code == 400
        assert body['code'] == '1200'
        assert body['message'] == 'UserName and Password required.'


class TestTokenGeneration:
    @allure.tag("api")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "dobrovolskiysv")
    @allure.epic("Аккаунт")
    @allure.feature("Генерация токена")
    @allure.story("Успешная")
    def test_successful_token_generation(self):
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
    def test_failed_token_generation(self):
        data = {"userName": project.config.login, "password": fake.password()}

        response = send_request('/Account/v1/GenerateToken', 'post', json=data)
        body = response.json()

        assert response.status_code == 200
        assert body.get('token') is None
        assert body.get('expires') is None
        assert body['status'] == 'Failed'
        assert body['result'] == 'User authorization failed.'


class TestUser:

    def test_post_user(self):
        data = {"userName": fake.user_name(), "password": fake.password()}
        # data = {"userName": "username", "password": "password"}

        response = send_request('/Account/v1/User', 'post', json=data)
        body = response.json()

        assert response.status_code == 201
        # assert body == True

    def test_post_existing_user(self):
        data = valid_credentials

        response = send_request('/Account/v1/User', 'post', json=data)
        body = response.json()

        assert response.status_code == 406
