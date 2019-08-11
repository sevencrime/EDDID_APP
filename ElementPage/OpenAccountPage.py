#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BasePage import BasePage


class OpenAccountPage(BasePage):

    easytoOpen_loc = (By.XPATH, "//*[text()='便捷开户']")

    def click_easytoOpen(self):
        self.find_element(*self.easytoOpen_loc).click()



