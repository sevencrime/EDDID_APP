#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from public.BaseView import BaseView
from selenium.webdriver.support import expected_conditions as EC

class IdentityInformationPage(BaseView):

    chineseresidents_loc = 'new UiSelector().className(\"android.widget.TextView\").textContains(\"我是内地居民\")'
    nextStep_loc = 'new UiSelector().className(\"android.widget.TextView\").textContains(\"下一步\")'
    passportMaterialFront = 'new UiSelector().className(\"android.widget.TextView\").textContains(\"请上传身份证人像面\")'
    passportMaterialback = 'new UiSelector().className(\"android.widget.TextView\").textContains(\"请上传身份证国徽面\")'


    def click_nextStep(self):
        self.find_uiautomator(self.nextStep_loc).click()

    # 选择所属地区--我是内地居民
    def click_chineseresidents(self):
        self.find_uiautomator(self.chineseresidents_loc).click()

    # 点击"请上传身份证人像面"
    def upload_passportMaterialFront(self):
        self.find_uiautomator(self.passportMaterialFront).click()

    # 点击"请上传身份证国徽面"
    def upload_passportMaterialback(self):
        pass


