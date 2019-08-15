#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ElementPage.IdentityInformation import IdentityInformation
from public.BaseView import BaseView


class publicFunc(BaseView):

    def click_nextStep(self):
        identity = IdentityInformation()
        identity.click_nextStep()
