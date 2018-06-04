import allure
import pytest

from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_login_valid_credentials(app):
    app.session.login('somethingphysician@example.com', 'test')
    sleep(5)
    with allure.step('Get welcome message'):
        greeting = get_text(app.driver, app.session.greeting_xp)
    with allure.step('Verification - valid credentials'):
        assert greeting == "My Patients"
