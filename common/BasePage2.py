#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time：2019/5/28 23:56

import os
import sys
import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(ROOT_DIR)


class WebTools(object):
    """selenium 底层API相关封装"""

    def __init__(self, path="webTools"):
        self.driver=webdriver.Chrome()
        self.Time_out = 5
        self.Time_poll = 0.5


    """
    浏览器相关方法：
    前进，后退，刷新，打开,获取Url，获取Title
    """

    # 前进浏览器
    def Forward(self):
        self.driver.forward()
        self.logger.info("前进浏览器")

    # 后退浏览器
    def Back(self):
        self.driver.back()
        self.logger.info("后退浏览器")

    # 刷新浏览器
    def Refresh(self):
        self.driver.refresh()
        self.logger.info("刷新浏览器")


    # 关闭浏览器
    def Quit(self):
        time.sleep(2)
        self.driver.quit()
        self.logger.info("关闭浏览器")

    # 关闭窗口
    def Close(self):
        self.driver.close()
        self.logger.info("关闭窗口")

    # 获取浏览器URL
    def Get_Url(self):
        time.sleep(1)
        url = self.driver.current_url
        self.logger.info("获取浏览器URL：" + "[" + str(url) + "]")
        return url

    # 获取浏览器Title
    def Get_title(self):
        time.sleep(1)
        title = self.driver.title
        self.logger.info("获取浏览器Title：" + "[" + str(title) + "]")
        return title

    """
    WebElement相关方法：
    提交表单，返回元素尺寸，返回元素文本，返回属性值，返回元素是否可见，睡眠，返回当前验证码
    """

    # 提交表单
    def Submit(self, by):
        self.find(by).submit()
        self.logger.info("提交表单：By" + "[" + str(by) + "]")

    # 返回元素尺寸
    def Get_size(self, by):
        time.sleep(1)
        size = self.find(by).size
        self.logger.info("返回元素尺寸：By" + "[" + str(by) + "]-" + str(size))
        return size

    # 返回元素文本
    def Get_text(self, by):
        time.sleep(1)
        text = self.find(by).text
        self.logger.info("返回元素尺寸：By" + "[" + str(by) + "]-" + str(text))
        return text

    # 返回属性值
    def Get_attribute(self, by, name):
        time.sleep(1)
        attribute = self.find(by).get_attribute(name)
        self.logger.info("返回属性值：By/name" + "[" + str(by) + "/" + str(name) + "]-" + str(attribute))
        return attribute

    # 返回元素是否可见
    def Get_result(self, by):
        time.sleep(1)
        result = self.find(by).is_displayed()
        self.logger.info("返回元素是否可见：By" + "[" + str(by) + "]-" + str(result))
        return result


    # 睡眠
    def Sleep(self, times):
        time.sleep(times)
        self.logger.info("睡眠：" + str(times))

    """
    鼠标事件相关方法：
    右击，悬停，双击，拖放
    """

    # 右击
    def Cilck_right(self, by):
        ActionChains(self.driver).context_click(self.find(by)).perform()
        self.logger.info("右击：By" + "[" + str(by) + "]")

    # 悬停
    def Move_to(self, by):
        ActionChains(self.driver).move_to_element(self.find(by)).perform()
        self.logger.info("悬停：By" + "[" + str(by) + "]")

    # 双击
    def Cilck_Double(self, by):
        ActionChains(self.driver).double_click(self.find(by)).perform()
        self.logger.info("双击：By" + "[" + str(by) + "]")

    # 拖放
    def Go_attribute(self, by_f, by_t):
        ActionChains(self.driver).drag_and_drop(self.find(by_f), self.find(by_t)).perform()
        self.logger.info("拖放：By" + "[" + str(by_f) + "->" + str(by_t) + "]")

    """
    键盘事件相关方法：
    回退字符，全选，复制，粘贴， 撤销，换行，空格，制表， 输入，单击，清除
    """

    # 回退字符
    def Keys_back(self, by):
        self.find(by).send_keys(Keys.BACK_SPACE)
        self.logger.info("回退字符：By" + "[" + str(by) + "]")

    # 全选
    def Keys_Ctrl_A(self, by):
        self.find(by).send_keys(Keys.CONTROL, "a")
        self.logger.info("全选：By" + "[" + str(by) + "]")

    # 复制
    def Keys_Ctrl_C(self, by):
        self.find(by).send_keys(Keys.CONTROL, "c")
        self.logger.info("复制：By" + "[" + str(by) + "]")

    # 粘贴
    def Keys_Ctrl_V(self, by):
        self.find(by).send_keys(Keys.CONTROL, "v")
        self.logger.info("粘贴：By" + "[" + str(by) + "]")

    # 撤销
    def Keys_Ctrl_Z(self, by):
        self.find(by).send_keys(Keys.CONTROL, "z")
        self.logger.info("撤销：By" + "[" + str(by) + "]")

    # 换行
    def Keys_Enter(self, by):
        self.find(by).send_keys(Keys.ENTER)
        self.logger.info("换行：By" + "[" + str(by) + "]")

    # 空格
    def Keys_Space(self, by):
        self.find(by).send_keys(Keys.SPACE)
        self.logger.info("空格：By" + "[" + str(by) + "]")

    # 制表
    def Keys_Tab(self, by):
        self.find(by).send_keys(Keys.TAB)
        self.logger.info("制表：By" + "[" + str(by) + "]")

    # 输入
    def Input(self, by, inputvalue):
        self.find(by).clear()
        self.find(by).send_keys(inputvalue)
        self.logger.info("输入：By" + "[" + str(str(by)) + "]")

    # 输入_子元素
    def Input_Child(self, by, by1, inputvalue):
        self.find_Child(by, by1).clear()
        self.find_Child(by, by1).send_keys(inputvalue)
        self.logger.info("输入_子元素：By" + "[" + str(by) + ">>>" + str(by1) + "]")

    # 单击
    def Click(self, by):
        self.find(by).click()
        self.logger.info("单击：By" + "[" + str(by) + "]")

    # 单击_子元素
    def Click_Child(self, by, by1):
        self.find_Child(by, by1).click()
        self.logger.info("单击_子元素：By" + "[" + str(by) + ">>>" + str(by1) + "]")

    # 清除
    def Clear(self, by):
        self.find(by).clear()
        self.logger.info("清除：By" + "[" + str(by) + "]")

    # 清除_子元素
    def Clear_Child(self, by, by1):
        self.find_Child(by, by1).clear()
        self.logger.info("清除_子元素：By" + "[" + str(by) + ">>>" + str(by1) + "]")

    # 确认警告框
    def Alert_accept(self):
        self.driver.switch_to_alert().accept()
        self.logger.info("确认警告框")

    # 取消警告框
    def Alert_dismiss(self):
        self.driver.switch_to_alert().dismiss()
        self.logger.info("取消警告框")

    # 返回警告框内容
    def Get_alert_text(self):
        text = self.driver.switch_to_alert().text
        self.logger.info("返回警告框内容：" + str(text))
        return text

    # 输入警告框内容
    def Input_alert_text(self, text):
        self.driver.switch_to_alert().send_keys(text)
        self.logger.info("输入警告框内容：" + str(text))

    # 返回所有Window句柄
    def Get_driver_windows(self):
        driver_windows = self.driver.window_handles
        self.logger.info("返回所有Window句柄：" + str(driver_windows))
        return driver_windows

    # 返回当前Window句柄
    def Get_driver_window(self):
        driver_window = self.driver.current_window_handle
        self.logger.info("返回当前Window句柄：" + str(driver_window))
        return driver_window

    # 切换Windows
    def Switch_window(self, window):
        self.driver.switch_to.window(window)
        self.logger.info("切换Windows：" + str(window))

    # 切换Frame
    def Switch_frame(self, by):
        self.driver.switch_to.frame(by)
        self.logger.info("切换Frame：By" + "[" + str(by) + "]")

    # 查找元素
    def find(self, by):
        try:
            element = WebDriverWait(self.driver, self.Time_out, self.Time_poll, "NoFindWebelement").until(
                EC.presence_of_element_located(by))
            return element
        except:
            log = ("未找到Webelement：By" + "[" + str(by) + "]截图：>>>" + self.get_windows_img())
            self.logger.info(log)

    # 查找子元素
    def find_Child(self, by, by1):
        try:
            element = self.driver.find_element(*by)
            time.sleep(1)
            element = element.find_element(*by1)
            return element
        except:
            log = ("未找到Webelement：By" + "[" + str(by) + ">>>" + str(by1) + "]截图：>>>" + self.get_windows_img())
            self.logger.info(log)

    # 查找元素们
    def finds(self, by):
        try:
            elements = WebDriverWait(self.driver, self.Time_out, self.Time_poll, "未找到Webelement").until(
                EC.presence_of_all_elements_located(by))
            return elements
        except:
            log = ("未找到Webelement：By" + "[" + str(by) + "]截图：>>>" + self.get_windows_img())
            self.logger.info(log)

    # 保存浏览器截图
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./testOutput/screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/testOutput/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            return rq + '.png'
        except:
            self.logger.info("截图失败")

    # 保存元素截图
    def get_element_img(self, by):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./testOutput/screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/testOutput/screenshots/'
        rq = "get_element_img"
        screen_name = file_path + rq + '.png'
        element = self.find(by)
        try:
            self.driver.save_screenshot(screen_name)
            left = element.location['x']
            top = element.location['y']
            right = element.location['x'] + element.size['width']
            bottom = element.location['y'] + element.size['height']
            im = Image.open(screen_name)
            im = im.crop((left, top, right, bottom))
            im.save(screen_name)
            return screen_name
        except:
            self.logger.info("元素截图失败")


