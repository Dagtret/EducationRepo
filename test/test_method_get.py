import httpx
from jsonschema import validate
from core.contracts import LIST_DATA_SCHEMA, LIST_USERS_DATA_SCHEMA

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

def test_list_users():
    response = httpx.get(host + endpoint_list_users)
    assert response.status_code == 200
    data = response.json()["data"]

    for item in data:
        validate(item, LIST_USERS_DATA_SCHEMA)
        assert item["email"].endswith(email_ends)
        assert str(item["id"]) in item["avatar"]

def test_single_user():
    response = httpx.get(host + endpoint_single_user)
    assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_USERS_DATA_SCHEMA)
    assert data["email"].endswith(email_ends)
    assert str(data["id"]) in data["avatar"]

def test_single_user_nf():
    response = httpx.get(host + endpoint_single_user_nf)
    assert response.status_code == 404

def test_list_resource():
    response = httpx.get(host + endpoint_list_resource)
    assert response.status_code == 200
    data = response.json()["data"]

    for item in data:
        validate(item, LIST_DATA_SCHEMA)
        assert item["color"].startswith(color_starts)
        assert hyphen in item["pantone_value"]

def test_single_resource():
    response = httpx.get(host + endpoint_single_resource)
    assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_DATA_SCHEMA)
    assert data["color"].startswith(color_starts)
    assert hyphen in data["pantone_value"]

def test_single_resource_nf():
    response = httpx.get(host + endpoint_single_resource_nf)
    assert response.status_code == 404