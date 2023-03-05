import pytest
import requests

from tests.conftest import api_base_url, valid_user, invalid_user
from utils.api_utils import get_user_info, create_user, update_user, delete_user, get_user_by_id


@pytest.mark.parametrize("user_id, expected_name", [(1, "George Bluth"), (2, "Janet Weaver")])
def test_get_user_info(api_base_url, user_id, expected_name):
    # Проверяем, что информация о пользователе с заданным ID возвращается корректно
    response = get_user_info(api_base_url, user_id)
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == expected_name

@pytest.mark.parametrize("name, job", [("John Doe", "Tester"), ("Jane Doe", "Developer")])
def test_create_user(self, name, job):
    # Проверяем, что новый пользователь может быть успешно создан
    response = create_user(name, job)
    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_delete_user(self, user_id):
    # Проверяем, что пользователь может быть удален
    response = delete_user(user_id)
    assert response.status_code == 204
    assert get_user_by_id(user_id).status_code == 404

def test_update_user(api_base_url):
    # Проверяем, что информация о пользователе может быть успешно обновлена
    user_id = 1
    updated_data = {"name": "George Bluth Sr.", "job": "Retired"}
    response = update_user(api_base_url, user_id, updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["job"] == updated_data["job"]

@pytest.mark.parametrize("non_existent_id, unexpected_name", [(2000, "Api Testerovich")])
def test_get_non_existing_user(api_base_url):
    # Проверяем, ответ на запрос о несуществующем пользователе
    response = get_user_info(api_base_url, non_existent_id)
    assert response.status_code == 404

def test_create_user_missing_field(api_base_url):
    # Проверяем возможность создания пользователя без обязательного поля
    payload = {
        "name": "morpheus"
    }
    response = requests.post(f'{api_base_url}/users', json=payload)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing required field: job'

# WEB тест для проверки отправки запроса через форму на главной странице и сравнения результата с API запросом
def test_web_request(base_url):
    response = requests.get('https://reqres.in/')
    csrf_token = response.cookies['csrf_token']

    payload = {
        "name": "morpheus",
        "job": "leader",
        "csrf_token": csrf_token
    }
    headers = {
        "Referer": "https://reqres.in/"
    }
    response = requests.post('https://reqres.in/api/users', data=payload, headers=headers)
    assert response.status_code == 201

    response_api = requests.get(f'{api_base_url}/users/{response.json()["id"]}')
    assert response_api.status_code == 200
    assert response.json()['name'] == response_api.json()['data']['first_name']
    assert response.json()['job'] == response_api.json()['data']['last_name']

# Параметризация тестов для получения списка пользователей
@pytest.mark.parametrize('page,per_page', [(1,2), (2,3)])
def test_list_users(base_url, page, per_page):
    response = requests.get(f'{base_url}/users?page={page}&per_page={per_page}')
    assert response.status_code == 200
    assert len(response.json()['data']) == per_page

@pytest.mark.parametrize("user, expected_status_code", [
    (valid_user, 200),
    (invalid_user, 400)
])
def test_register_user(user, expected_status_code):
    response = register_user(user["email"], user["password"])
    assert response.status_code == expected_status_code
