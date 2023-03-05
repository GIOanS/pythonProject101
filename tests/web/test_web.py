import pytest
from selenium import webdriver
from utils.web_utils import click_button, get_result_from_modal, valid_user, invalid_user, url_register, \
    fill_form


def test_homepage_loads_successfully(self, driver):
    # Проверяем доступность домашней страницы
    homepage = get_homepage(driver)
    assert homepage.is_loaded()

@pytest.mark.parametrize("input_text, expected_text", [("Test1", "Test1"), ("Test2", "Test2")])
def test_submit_button_returns_correct_result(self, driver, input_text, expected_text):
    # Проверяем корректность ответа при нажатии на кнопку
    homepage = get_homepage(driver)
    homepage.fill_input(input_text)
    result_modal = click_button(homepage)
    assert result_modal.is_loaded()
    assert get_result_from_modal(result_modal) == expected_text

@pytest.mark.parametrize("name, job", [("John Doe", "Software Developer"), ("Jane Smith", "Data Analyst")])
def test_fill_and_submit_form(base_url, driver, name, job):
    # Проверяем заполнение и отправку формы
    open_page(driver, base_url)
    form_data = {"name": name, "job": job}
    fill_form(driver, form_data)
    submit_form(driver)
    assert "successfully created" in driver.page_source

@pytest.mark.parametrize("user", [
    pytest.param(valid_user, id="valid_user"),
    pytest.param(invalid_user, id="invalid_user")
])
def test_signup_form(driver, signup_url, user):
    # Проверяем форму входа
    open_signup_page(driver, signup_url)
    submit_signup_form(driver, user)
    assert driver.current_url == url_register
    assert "Thank you for registering" in driver.page_source