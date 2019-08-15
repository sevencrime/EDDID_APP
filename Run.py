#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
import os


pytest.main(['-v', os.getcwd()+r'\EDDID_APP\Case', '--pdb', '--alluredir', os.getcwd() + r'\EDDID_APP\report\xml'])
print("生成html")
os.popen("allure generate {xml} -o {html} --clean".format(xml = os.getcwd()+r'\EDDID_APP\report\xml', html = os.getcwd()+r'\EDDID_APP\report\html'))
print("生成成功")