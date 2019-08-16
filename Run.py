#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
import os


pytest.main(['-v', os.getcwd()+r'\EDDID_APP\Case', '--pdb', '--alluredir', os.getcwd() + r'\EDDID_APP\report\xml'])
os.popen("allure generate {xml} -o {html} --clean".format(xml = os.getcwd()+r'\EDDID_APP\report\xml', html = os.getcwd()+r'\EDDID_APP\report\html'))