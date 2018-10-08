from appium import webdriver
import pytest


class Driver():

    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            "automationName": "Appium",
            # "automationName": "uiautomator2",
            "appActivity": "com.leia.leialoft.ui.splash.view.SplashActivity",
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "3a90b04d",
            "appPackage": "com.leia.leialoft",
            "noReset": "true",
            # "autoGrantPermissions": "true"
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver
