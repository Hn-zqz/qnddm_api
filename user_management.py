#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：^_^
# @Time：2021/5/16 19:11
# @Email:2560500412@qq.com
import os
from common.HTMLTestRunnerNew import HTMLTestRunner
import common.BeautifulReport as brf
from test_case import user_management
from report import postion
import unittest,time
suit=unittest.TestSuite()
loder=unittest.TestLoader()
suit.addTest(loder.loadTestsFromTestCase(user_management.Test_user_management))


path=postion.get_cwd()
time=time.strftime("%Y%m%d%H%M%S")
# path=os.path.join(path,time)
# path=path+".html"
# with open(path,"wb") as f:
#     report=HTMLTestRunner(stream=f,verbosity=1,title="禅道登录用例测试报告",description="第不知道多少份测试报告",tester="zz")
#     report.run(suit)
report=brf.BeautifulReport(suit)
report.report(description="Test",filename=f"{time}测试报告",report_dir=path)
