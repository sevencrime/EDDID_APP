#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
from appium import webdriver

@pytest.fixture(scope="session", autouse=True)
def driver():
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': platformVersion,
        'deviceName': '127.0.0.1:7555',
        'appPackage': 'io.newtype.eddid.app',
        'appActivity': 'com.bartech.app.MainActivity',
        # 'unicodeKeyboard': True,
        # 'resetKeyboard': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield driver
    print("所有用例执行完成, 关闭driver")
    driver.quit()