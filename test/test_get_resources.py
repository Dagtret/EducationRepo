import httpx
from jsonschema import validate
from core.contracts import LIST_DATA_SCHEMA
import allure

host = "https://reqres.in/"
endpoint_list_resource = "api/unknown"
endpoint_single_resource = "api/unknown/2"
endpoint_single_resource_nf = "api/unknown/23"
email_ends = "@reqres.in"
color_starts = "#"
hyphen = "-"

@allure.suite("Проверка списка ресурсов")
@allure.title("Проверяем общий списов ресурсов")
def test_list_resource():
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_list_resource}"):
        response = httpx.get(host + endpoint_list_resource)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200
    data = response.json()["data"]

    for item in data:
        with allure.step("Проверяем элемент из списка"):
            validate(item, LIST_DATA_SCHEMA)
            with allure.step(f"Проверяем, что значение color начинается с {color_starts}"):
                assert item["color"].startswith(color_starts)
            with allure.step("Проверяем, что в pantone_value есть дефис"):
                assert hyphen in item["pantone_value"]

@allure.suite("Проверка списка ресурсов")
@allure.title("Проверяем конкретный ресурс")
def test_single_resource():
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_single_resource}"):
        response = httpx.get(host + endpoint_single_resource)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_DATA_SCHEMA)
    with allure.step(f"Проверяем, что значение color начинается с {color_starts}"):
        assert data["color"].startswith(color_starts)
    with allure.step("Проверяем, что в pantone_value есть дефис"):
        assert hyphen in data["pantone_value"]

@allure.suite("Проверка списка ресурсов")
@allure.title(f"Проверяем какой ответ приходит по методу {endpoint_single_resource_nf}")
def test_single_resource_nf():
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_single_resource_nf}"):
        response = httpx.get(host + endpoint_single_resource_nf)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 404