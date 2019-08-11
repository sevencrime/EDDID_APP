#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BasePage import BasePage


class BottomBarPage(BasePage):

    opening_loc = (By.XPATH, "//*[@resource-id='io.newtype.eddid.app:id/nav_menu_id']//*[@text='开户']")
    btn_start_loc = (By.ID, "io.newtype.eddid.app:id/btn_start")

    def click_btnStart(self):
        self.find_element(*self.btn_start_loc).click()

    def click_opening(self):
        opening = self.find_element(*self.opening_loc).click()



