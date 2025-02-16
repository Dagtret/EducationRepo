import httpx
from jsonschema import validate
from core.contracts import LIST_USERS_DATA_SCHEMA
import allure

host = "https://reqres.in/"
endpoint_delete_users = "api/users/2"

@allure.suite('Проверка удаления пользователя')
@allure.title('Проверяем удаление пользователя')
def test_list_users():
    with allure.step(f"Делаем запрос по адресу: {host + endpoint_delete_users}"):
        response = httpx.delete(host + endpoint_delete_users)
    with allure.step("Проверяем код ответа"):
        assert response.status_code == 204