from appium import webdriver
import pytest
from infrastracture import test_configuration
from infrastracture import workiz_application


@pytest.fixture(scope="class")
def create_driver_on_landing_page(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", test_configuration.desired_capabilities)
    driver.desired_capabilities
    driver.implicitly_wait(10)
    workiz_app = workiz_application.WorkizApplication(driver, False)
    request.cls.workiz_app = workiz_app


@pytest.fixture(scope="class")
def create_driver_after_login(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", test_configuration.desired_capabilities)
    driver.implicitly_wait(10)
    workiz_app = workiz_application.WorkizApplication(driver)
    request.cls.workiz_app = workiz_app

