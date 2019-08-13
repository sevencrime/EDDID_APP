#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure


pytest.main(['-v', r'D:\Test\EDDID_APP\Case', '--pdb', '--alluredir', 'D:/Test/EDDID_APP/report/xml'])
