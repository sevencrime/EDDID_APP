#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

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
        with allure.step('点击登录按钮'):
            register.click_login()
