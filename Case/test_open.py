#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
import allure

from ElementPage.BottomBarPage import BottomBarPage
from public.BasePage import BasePage


class Test_Open():
    # 启动APP, 进入开户界面

    allure.feature("启动APP")
    def test_open(self, driver):
        pass
        # BottomBarPage(driver).click_opening()


if __name__ == '__main__':
    pytest.main(["-s","test_open.py"])
