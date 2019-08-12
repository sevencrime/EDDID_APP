#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from public.BaseView import BaseView
from selenium.webdriver.support import expected_conditions as EC

class bottomBarPage(BaseView):

    opening_loc = (By.XPATH, "//*[@resource-id='io.newtype.eddid.app:id/nav_menu_id']//*[@text='开户']")
    btn_start_loc = (By.ID, "io.newtype.eddid.app:id/btn_start")
    Permission_loc = (By.XPATH, "//*[@text='允许']")

    def click_btnStart(self):
        self.find_element(*self.btn_start_loc).click()

    def click_opening(self):
        opening = self.find_element(*self.opening_loc).click()


    def always_allow(self, number=5):
        for i in range(5):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(self.Permission_loc))
                e.click()
            except:
                pass
