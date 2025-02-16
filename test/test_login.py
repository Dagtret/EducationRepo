import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTER_USER_SCHEMA_SUCCESSFUL,LOGIN_USER_SCHEMA_SUCCESSFUL, LOGIN_AND_REGISTER_USER_SCHEMA_UNSUCCESSFUL
import allure

host = "https://reqres.in/"
endpoint_login = "api/login"

json_file = open('core/new_users_data.json')
users_data = json.load(json_file)

@pytest.mark.parametrize('users_data', users_data)
@allure.suite('Проверка успешной авторизации')
@allure.title('Проверяем авторизацию пользователей из списка')
def test_login_successful(users_data):
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_login}'):
        response = httpx.post(host + endpoint_login, json=users_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    validate(response.json(), LOGIN_USER_SCHEMA_SUCCESSFUL)

@allure.suite('Проверка авторизации с ошибкой')
@allure.title('Проверяем авторизацию пользователя без поля "password"')
def test_register_unsuccessful():
    body = {
        "email": "eve.holt@reqres.in"
    }
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_login}'):
        response = httpx.post(host + endpoint_login, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400
    validate(response.json(), LOGIN_AND_REGISTER_USER_SCHEMA_UNSUCCESSFUL)