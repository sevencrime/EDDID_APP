#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from public.GlobalMap import GlobalMap


class BaseView(object):

    gbm = GlobalMap()

    def __init__(self, driver):
        self.driver = driver

    # 重写元素定位方法
    def find_element(self, *loc):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(loc))

            # WebDriverWait(self.driver, 20).until(
            #     EC.visibility_of_element_located(loc))

            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
            flag = False
            return flag

    def find_elements(self, *loc):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(loc))

            return self.driver.find_elements(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
            flag = False
            return flag

    def find_uiautomator(self, uiautomator):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_android_uiautomator(uiautomator).is_displayed())
            return self.driver.find_element_by_android_uiautomator(uiautomator)

        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, uiautomator))
            flag = False
            return flag


