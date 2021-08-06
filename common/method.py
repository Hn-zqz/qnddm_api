#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：^_^
# @Time：2020/1/16 8:47
# @Email:2560500412@qq.com

from selenium import webdriver
def get_alert_text(wk):
    return  wk.switch_to_alert().text