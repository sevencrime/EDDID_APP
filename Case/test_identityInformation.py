#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure

from Case.publicFunc import publicFunc
from ElementPage.IdentityInformationPage import IdentityInformationPage


@allure.feature("选择所属地区和开户准备")
class Test_identityInformation():


    @allure.story("选择所属地区页面")
    @pytest.mark.run(order=3)
    def test_SelectAreaforchinese(self, driver):
        identity = IdentityInformationPage(driver)
        with allure.step("选择中国居民"):
            identity.click_chineseresidents()


    @allure.story("开户准备")
    @pytest.mark.run(order=4)
    def test_AccountOpenPreparation(self, driver):
        with allure.step("开户准备页面点击下一步"):
            pf = publicFunc(driver)
            pf.click_nextStep()

    @allure.story("上传身份证")
    @pytest.mark.run(order=4)
    def test_IdentityInformation(self, driver):
        with allure.step("点击身份证正面框"):

