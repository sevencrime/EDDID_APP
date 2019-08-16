#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ElementPage.IdentityInformationPage import IdentityInformationPage
from ElementPage.registerPage import registerPage
from public.BaseView import BaseView


class publicFunc(BaseView):

    def click_nextStep(self):
        identity = IdentityInformationPage(self.driver)
        identity.click_nextStep()

    def wait_loading(self):
        register = registerPage(self.driver)
        register.wait_loading()
