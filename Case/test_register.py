#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import allure
import pytest

from Case.publicFunc import publicFunc
from ElementPage.registerPage import registerPage

@allure.feature("登录账户")
class Test_register():

    @allure.story("登录账户")
    @pytest.mark.run(order = 2)
    def test_login(self, driver):
        register = registerPage(driver)
        with allure.step("注册页面点击'去登陆'按钮"):
            register.click_login_btn()
        with allure.step("输入账户"):
            register.click_phoneNumber()
        with allure.step("输入密码"):
            register.click_paswd()
            # 点击系统返回键, 防止登录按钮被挡住
            # driver.keyevent(4)
        with allure.step('点击登录按钮'):
            # import pdb; pdb.set_trace()
            time.sleep(5)
            register.click_login()
        with allure.step('判断是否进入开户表单界面'):
            publicFunc(driver).wait_loading()
