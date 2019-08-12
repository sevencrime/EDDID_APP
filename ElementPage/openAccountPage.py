#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from public.BaseView import BaseView


class openAccountPage(BaseView):

    easytoOpen_loc = "new UiSelector().className(\"android.widget.TextView\").textContains(\"便捷开户\")"

    def click_easytoOpen(self):
        # import pdb; pdb.set_trace()
        self.find_uiautomator(self.easytoOpen_loc).click()

