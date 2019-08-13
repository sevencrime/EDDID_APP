#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BaseView import BaseView


class registerPage(BaseView):

    login_btn_loc = 'new UiSelector().textContains("去登录")'
    phone_number_loc = (By.XPATH, "//android.widget.EditText[@text='请输入手机号']")
    paswd_loc = (By.XPATH, "//android.widget.EditText[@text='请输入密码']")
    login_loc = 'new UiSelector().className(\"android.widget.TextView\").textContains(\"登录\")'

    def click_login_btn(self):
        self.find_uiautomator(self.login_btn_loc).click()

    def click_phoneNumber(self):
        self.find_element(*self.phone_number_loc).send_keys("15089514626")

    def click_paswd(self):
        self.find_element(*self.paswd_loc).send_keys("abcd1234")

    def click_login(self):
        self.find_uiautomator(self.login_loc).click()