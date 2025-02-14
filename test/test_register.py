import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTER_USER_SCHEMA_SUCCESSFUL, LOGIN_AND_REGISTER_USER_SCHEMA_UNSUCCESSFUL
import allure

host = "https://reqres.in/"
endpoint_register = "api/register"

json_file = open('core/new_users_data.json')
users_data = json.load(json_file)

@pytest.mark.parametrize('users_data', users_data)
@allure.suite('Проверка успешной регистарции')
@allure.title('Проверяем регистарцию пользователей из списка')
def test_register_successful(users_data):
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_register}'):
        response = httpx.post(host + endpoint_register, json=users_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    validate(response.json(), REGISTER_USER_SCHEMA_SUCCESSFUL)

@allure.suite('Проверка регистрации с ошибкой')
@allure.title('Проверяем регистарцию пользователя без поля "password"')
def test_register_unsuccessful():
    body = {
        "email": "eve.holt@reqres.in"
    }
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_register}'):
        response = httpx.post(host + endpoint_register, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400
    validate(response.json(), LOGIN_AND_REGISTER_USER_SCHEMA_UNSUCCESSFUL)
