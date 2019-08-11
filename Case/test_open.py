#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
import allure

from ElementPage.OpenAccountPage import OpenAccountPage
from ElementPage.BottomBarPage import BottomBarPage
from public.BasePage import BasePage


class Test_Open():
    # 启动APP, 进入开户界面

    allure.feature("启动APP, 进入开户界面")
    def test_open(self, driver):
        bar = BottomBarPage(driver)
        import pdb; pdb.set_trace()
        # 点击开始使用
        bar.click_btnStart()
        # 点击开户按钮
        bar.click_opening()
        # 点击便捷开户
        OpenAccountPage().click_easytoOpen()


if __name__ == '__main__':
    pytest.main(["-s","test_open.py"])
