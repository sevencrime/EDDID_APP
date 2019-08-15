#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
import allure
import time
from ElementPage.bottomBarPage import bottomBarPage
from ElementPage.registerPage import registerPage
from public.GlobalMap import GlobalMap


@allure.feature("启动APP, 进入开户界面")
class Test_Open():
    # 启动APP, 进入开户界面
    gbm = GlobalMap()

    @allure.story("点击便捷开户")
    @pytest.mark.run(order=1)
    def test_open(self, driver):
        bar = bottomBarPage(driver)
        with allure.step("处理弹出权限"):
            bar.always_allow()
        if self.gbm.get_value("trading") == True:
            with allure.step("底部选择开户菜单"):
                # 点击开始使用
                bar.click_btnStart()
                # 点击开户按钮
                bar.click_opening()

        with allure.step("点击便捷开户"):
            # 点击便捷开户
            print("start**********", time.asctime( time.localtime(time.time()) ))
            registerPage(driver).click_easytoOpen()
            print("end**********", time.asctime( time.localtime(time.time()) ))



if __name__ == '__main__':
    pytest.main(["-s","test_open.py", '--alluredir', '../report/xml'])
