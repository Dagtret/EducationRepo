import httpx
from jsonschema import validate
import allure
import datetime
from core.contracts import UPDATE_USER_SCHEMA

host = "https://reqres.in/"
endpoint_update_user = "api/users/2"

@allure.suite('Проверка изменения данных пользователя методом put')
@allure.title('Проверяем изменение данных пользователя с полями "name" и "job"')
def test_update_user_with_name_and_job():
    body = {
        "name": "Sergey",
        "job": "AQA Engineer"
    }
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_update_user}'):
        response = httpx.put(host + endpoint_update_user, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    currant_date = str(datetime.datetime.utcnow())
    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "name" в теле ответа соответствует полю "name" в теле запроса'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что поле "job" в теле ответа соответствует полю "job" в теле запроса'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что время изменения соответствует текущему времени'):
        assert update_date[0:16] == currant_date[0:16]

@allure.suite('Проверка изменения данных пользователя методом put')
@allure.title('Проверяем изменение данных пользователя без поля "name"')
def test_update_user_without_job():
    body = {
        "job": "AQA Engineer"
    }
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_update_user}'):
        response = httpx.put(host + endpoint_update_user, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    currant_date = str(datetime.datetime.utcnow())
    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "job" в теле ответа соответствует полю "job" в теле запроса'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что время изменения соответствует текущему времени'):
        assert update_date[0:16] == currant_date[0:16]

@allure.suite('Проверка изменения данных пользователя методом put')
@allure.title('Проверяем изменение данных пользователя без поля "job"')
def test_update_user_without_name():
    body = {
        "name": "Sergey"
    }
    with allure.step(f'Делаем запрос по адресу: {host + endpoint_update_user}'):
        response = httpx.put(host + endpoint_update_user, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    currant_date = str(datetime.datetime.utcnow())
    validate(response_json, UPDATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "name" в теле ответа соответствует полю "name" в теле запроса'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что время изменения соответствует текущему времени'):
        assert update_date[0:16] == currant_date[0:16]