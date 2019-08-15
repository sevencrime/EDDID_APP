#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure

from Case.publicFunc import publicFunc
from ElementPage.IdentityInformation import IdentityInformation


@allure.feature("选择所属地区和开户准备")
class Test_identityInformation():


    @allure.story("选择所属地区页面")
    @pytest.mark.run(order=3)
    def test_SelectAreaforchinese(self, driver):
        identity = IdentityInformation(driver)
        pf = publicFunc(driver)
        with allure.step("选择中国居民"):
            self.identity.click_chineseresidents()

        with allure.step("开户准备页面点击下一步"):
            self.pf.click_nextStep()