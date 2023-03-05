import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/"

@pytest.fixture(scope="module")
def api_base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope='session')
def api_client(base_url):
    return requests.Session()

@pytest.fixture(scope='session')
def web_client(base_url):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def driver(self, request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture(scope="module")
def valid_user():
    user = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return user

@pytest.fixture(scope="module")
def invalid_user():
    user = {
        "email": "sydney@fife"
    }
    return user

@pytest.fixture(scope="module")
def url_register():
    return "https://reqres.in/api/register"


