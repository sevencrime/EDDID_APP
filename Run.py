#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
import os


pytest.main(['-v', r'D:\Test\EDDID_APP\Case', '--pdb', '--alluredir', os.getcwd() + r'\EDDID_APP\report\xml'])
