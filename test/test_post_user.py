import httpx
from jsonschema import validate
import allure
from core.contracts import CREATE_USER_SCHEMA
import datetime

host = "https://reqres.in/"
endpoint_create_user = "api/users"

@allure.suite("Проверка создания пользователя")
@allure.title('Проверяем создание пользователя с полями "name" и "job"')
def test_create_user_with_name_and_job():
    body = {
        "name": "Sergey",
        "job": "AQA Engineer"
    }
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_create_user}"):
        response = httpx.post(host + endpoint_create_user, json=body)
    response_json = response.json()
    creation_date = response_json["createdAt"].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())
    with allure.step("Проверяем код ответа"):
        assert  response.status_code == 201
    validate(response_json, CREATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "name" в теле ответа соответствует полю "name" в теле запроса'):
        assert response_json["name"] == body["name"]
    with allure.step('Проверяем, что поле "job" в теле ответа соответствует полю "job" в теле запроса'):
        assert response_json["job"] == body["job"]
    with allure.step('Проверяем, что время создания соответствует текущему времени'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite("Проверка создания пользователя")
@allure.title('Проверяем создание пользователя без поля "name"')
def test_create_user_without_name():
    body = {
        "job": "AQA Engineer"
    }
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_create_user}"):
        response = httpx.post(host + endpoint_create_user, json=body)
    response_json = response.json()
    creation_date = response_json["createdAt"].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 201
    validate(response_json, CREATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "job" в теле ответа соответствует полю "job" в теле запроса'):
        assert response_json["job"] == body["job"]
    with allure.step('Проверяем, что время создания соответствует текущему времени'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite("Проверка создания пользователя")
@allure.title('Проверяем создание пользователя без поля "job"')
def test_create_user_without_job():
    body = {
        "name": "Sergey"
    }
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_create_user}"):
        response = httpx.post(host + endpoint_create_user, json=body)
    response_json = response.json()
    creation_date = response_json["createdAt"].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 201
    validate(response_json, CREATE_USER_SCHEMA)
    with allure.step('Проверяем, что поле "name" в теле ответа соответствует полю "name" в теле запроса'):
        assert response_json["name"] == body["name"]
    with allure.step('Проверяем, что время создания соответствует текущему времени'):
        assert creation_date[0:16] == current_date[0:16]