#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from public.BaseView import BaseView
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class registerPage(BaseView):

    login_btn_loc = 'new UiSelector().textContains("去登录")'
    phone_number_loc = (By.XPATH, "//android.widget.EditText[@text='请输入手机号']")
    paswd_loc = (By.XPATH, "//android.widget.EditText[@text='请输入密码']")
    # login_loc = (By.XPATH, "//android.widget.TextView[@text='登录']/parent::android.view.ViewGroup")
    login_loc = (By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='登录']")
    easytoOpen_loc = "new UiSelector().className(\"android.widget.TextView\").textContains(\"便捷开户\")"

    def wait_loading(self):
        progressbar_loc = (By.CLASS_NAME, "android.widget.ProgressBar")
        try:
            WebDriverWait(self.driver, 30).until_not(
                EC.presence_of_element_located(progressbar_loc))
        except TimeoutException:
            print("失败, 请求超时")

    def click_easytoOpen(self):
        # import pdb; pdb.set_trace()
        self.find_uiautomator(self.easytoOpen_loc).click()

    def click_login_btn(self):
        self.find_uiautomator(self.login_btn_loc).click()

    def click_phoneNumber(self):
        self.find_element(*self.phone_number_loc).send_keys(self.gbm.get_value("phone_number"))

    def click_paswd(self):
        self.find_element(*self.paswd_loc).send_keys(self.gbm.get_value("paswd"))

    def click_login(self):
        # self.find_uiautomator(self.login_loc).click()
        self.find_element(*self.login_loc).click()