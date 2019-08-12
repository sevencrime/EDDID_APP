#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BaseView import BaseView


class registerPage(BaseView):

    login_btn_loc = 'new UiSelector().textContains("去登录")'


    def click_login_btn(self):
        self.find_uiautomator(self.login_btn_loc).click()
