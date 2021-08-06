#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time：2019/5/27 22:32
# @Email:122712084@qq.com

#封装基本函数---执行日志、异常处理、失败截图
#所有页面的公共部分
import logging
import time
import os
import Outputs.getcwd as getcwd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from lxml import etree
import requests

from common import defs


class BasePage:
    def __init__(self,driver=0):
        self.driver=driver
   #封装日志
    def get_log(self):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 设置日志存放路径，日志文件名
        # 获取本地时间，转换为设置的格式
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        # 设置所有日志和错误日志的存放路径
        path = getcwd.get_cwd()
        # 通过getcwd.py文件的绝对路径来拼接日志存放路径
        all_log_path = os.path.join(path, 'Logs/All_Logs/')
        error_log_path = os.path.join(path, 'Logs/Error_Logs/')
        # 设置日志文件名
        all_log_name = all_log_path + rq + '.log'
        error_log_name = error_log_path + rq + '.log'

        # 创建handler
        # 创建一个handler写入所有日志
        fh = logging.FileHandler(all_log_name, encoding='utf8')
        fh.setLevel(logging.INFO)
        # 创建一个handler写入错误日志
        eh = logging.FileHandler(error_log_name, encoding="utf8")
        eh.setLevel(logging.ERROR)
        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        if not logger.handlers:
            logger.addHandler(fh)
            logger.addHandler(eh)
            logger.addHandler(ch)
        return logger


    #等待元素可见
    def wait_eleVisible(self,locator,time=30):
        log=self.get_log()
        log.info("等待元素{}可见".format(locator))
        try:
            #开始等待的时间
            start=datetime.datetime.now()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            #结束等待的时间
            end=datetime.datetime.now()
            #求一个差值，写在日志当中。
            log.info("等待时长")
        except :
           log.error("等待元素可见失败")
           self.save_screenshot()
            #截图操作

#
#     #等待元素存在
#     def wait_elePresence(self):
#         pass
#
#     #查找元素
#     def get_element(self,locator):
#         logging.info("查找元素:{}".format(locator))
#         try:
#             self.driver.find_element(*locator)
#         except:
#             logging.exception("没招到")
#             #截图
#
#
#     #点击操作
#     def click_element(self):
#         pass
#     #输入操作
#     def input_text(self):
#         #找元素
#         ele=self.get_element()
#
#     #获取元素的文本内容
#     def get_text(self):
#         pass
#     #获取元素的属性
#
#     def get_elment_attribute(self):
#         pass
#     #alert处理
#     def alert_action(self,action="accept"):
#         pass
#     #iframe切换
#     def swtich_iframe(self):
#         pass
#     #滚动条处理
#
    #截图操作
    def save_screenshot(self):
        """
              截图并保存在根目录下的Screenshots文件夹下
              :param none:
              """
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("开始截图并保存")

        except Exception as e:
            logging.error("出现异常", format(e))




