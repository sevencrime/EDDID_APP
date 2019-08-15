#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

import pytest
from appium import webdriver

from public.GlobalMap import GlobalMap


@pytest.fixture(scope="session", autouse=True)
def confini():
    gbm = GlobalMap()
    gbm.set_value(trading=True)
    gbm.set_value(phone_number = "15089514620")
    gbm.set_value(paswd = "abcd1234")


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
        # 'appActivity': 'com.bartech.app.main.launcher.LauncherActivity',
        'appActivity': 'io.newtype.eddid.app.MainActivity',
        'newCommandTimeout' : 200
        # 'unicodeKeyboard': True,
        # 'resetKeyboard': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield driver
    print("所有用例执行完成, 关闭driver")
    driver.quit()
    print("正在生成html报告")
    # import pdb; pdb.set_trace()
    # os.popen("allure generate ./report/xml -o ./report/html --clean")
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))