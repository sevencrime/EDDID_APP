#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

import pytest
from appium import webdriver

@pytest.fixture(scope="session", autouse=True)
def driver():
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    # 读取设备 id
    readDeviceId = list(os.popen('adb devices').readlines())
    # 正则表达式匹配出 id 信息
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': platformVersion,
        'deviceName': deviceId,
        'appPackage': 'io.newtype.eddid.app',
        'appActivity': 'com.bartech.app.main.launcher.LauncherActivity',
        'newCommandTimeout' : 120
        # 'unicodeKeyboard': True,
        # 'resetKeyboard': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield driver
    print("所有用例执行完成, 关闭driver")
    driver.quit()