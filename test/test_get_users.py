import httpx
from jsonschema import validate
from core.contracts import LIST_USERS_DATA_SCHEMA
import allure

host = "https://reqres.in/"
endpoint_list_users = "api/users?page=2"
endpoint_single_user = "api/users/2"
endpoint_single_user_nf = "api/users/23"
endpoint_list_resource = "api/unknown"
endpoint_single_resource = "api/unknown/2"
endpoint_single_resource_nf = "api/unknown/23"
email_ends = "@reqres.in"
color_starts = "#"
hyphen = "-"

@allure.suite("Проверка запросов данных пользователей")
@allure.title("Проверяем получение списка пользователей")
def test_list_users():
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_list_users}"):
        response = httpx.get(host + endpoint_list_users)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200
    data = response.json()["data"]

    for item in data:
        with allure.step("Проверяем элемент из списка"):
            validate(item, LIST_USERS_DATA_SCHEMA)
            with allure.step(f"Проверяем, что Email заканчивается на {email_ends}"):
                assert item["email"].endswith(email_ends)
            with allure.step(f'Проверяем, что значение id попадает в значение avatar'):
                assert str(item["id"]) in item["avatar"]

@allure.suite("Проверка запросов данных пользователей")
@allure.title("Проверяем получение данных пользователя")
def test_single_user():
    with allure.step(f"Делаем запрос по адресу {host + endpoint_single_user}"):
        response = httpx.get(host + endpoint_single_user)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_USERS_DATA_SCHEMA)
    with allure.step(f"Проверяем, что значение email заканчивается на {email_ends}"):
        assert data["email"].endswith(email_ends)
    with allure.step(f'Проверяем, что значение id попадает в значение avatar'):
        assert str(data["id"]) in data["avatar"]

@allure.suite("Проверка запросов данных пользователей")
@allure.title(f"Проверяем какой ответ приходит по методу {endpoint_single_user_nf}")
def test_single_user_nf():
    with allure.step(f"Делаем запрос по адресу {host + endpoint_single_user_nf}"):
        response = httpx.get(host + endpoint_single_user_nf)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 404