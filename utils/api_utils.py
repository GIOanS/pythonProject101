import requests

from tests.conftest import base_url


def send_get_request(url):
    response = requests.get(url)
    return response

def send_post_request(url, data):
    response = requests.post(url, json=data)
    return response

def check_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Unexpected status code: {response.status_code}"


def get_user_info(user_id):
    url = f'https://reqres.in/api/users/{user_id}'
    response = requests.get(base_url)
    return response.json()


def get_user_by_id(user_id):
    url = f'https://reqres.in/api/users/{user_id}'
    response = requests.get(base_url)
    response.raise_for_status()
    return response.json()


