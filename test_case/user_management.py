#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：^_^
# @Time：2021/5/16 18:31
# @Email:2560500412@qq.com
from test_data import postion
import unittest
import requests
from common import defs
import ast
from urllib import  parse
from common.myddt import ddt,data,unpack
from common import basepage
path=postion.get_cwd()
users_save_data=defs.row_column_read_datas(path+"/user_management.xlsx","users_save",row=2)
users_chanageaccountAction_save_data=defs.row_column_read_datas(path+"/user_management.xlsx","users_chanageaccountAction_save",row=2)
users_ajax=defs.row_column_read_datas(path+"/user_management.xlsx","users_ajax",row=2)

@ddt
class Test_user_management(unittest.TestCase):
    def setUp(self):
        self.headers={"Cookie":"JSESSIONID=b08930c8-1e06-48bc-9469-faddc1eeb7ee; sys__username=; sys__password=",
         "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        self.log=basepage.BasePage().get_log()

    # def tearDown(self):
    #     self.log.removeHandler(self.log.handlers[0])
    #     self.log.removeHandler(self.log.handlers[0])
    #     self.log.removeHandler(self.log.handlers[0])

    @data(*users_save_data)
    @unpack
    def test_user_save(self,title,url,data,expect):#新增用户接口
        dict_data=ast.literal_eval(data)
        dict_data["record"]=defs.get_record(self.headers)
        if title not in ["账号名称为空","账号名称已存在"]:
            dict_data["account"]=defs.get_account()
        if title not in ["手机号为空","手机号已存在","手机号错误"]:
            dict_data["mobile"]=defs.get_mobile()
        self.log.info(f"开始执行\t{title}\t测试用例")
        r=requests.post(url=url,data=dict_data,headers=self.headers)
        self.log.info("正在进行对比")
        self.log.info(f"case:{title}，\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n预期结果{expect}\n")
        self.assertIn(expect,r.text)

    @data(*users_chanageaccountAction_save_data)
    @unpack
    def test_users_chanageaccountAction_save(self,title,url,data,expect):#修改账号名称接口
        dict_data=ast.literal_eval(data)
        if title=="修改账号名称为正确数据":
            dict_data["account"]=defs.get_account()
        self.log.info(f"开始执行\t{title}\t测试用例")
        r=requests.post(url=url,data=dict_data,headers=self.headers)
        self.log.info("正在进行对比")
        self.log.info(f"case:{title}，\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n预期结果{expect}\n")
        self.assertIn(expect,r.text)

    @data(*users_ajax)
    @unpack
    def test_users_ajax(self,title,url,data,expect):#用户禁用和启用接口
        self.log.info(f"开始执行\t{title}\t测试用例")
        r = requests.post(url=url, data=ast.literal_eval(data), headers=self.headers)
        self.log.info("正在进行对比")
        self.log.info(f"case:{title}，\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n预期结果{expect}\n")
        self.assertIn(expect, r.text)

