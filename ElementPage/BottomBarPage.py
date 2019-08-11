#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BasePage import BasePage


class BottomBarPage(BasePage):

    opening_loc = (By.XPATH, "//*[@resource-id='io.newtype.eddid.app:id/nav_menu_id']//*[@text='开户']")


    def click_opening(self):
        opening = self.find_element(*self.opening_loc).click()



