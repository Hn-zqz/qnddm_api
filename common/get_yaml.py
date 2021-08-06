#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：^_^
# @Time：2020/3/9 14:59
# @Email:2560500412@qq.com
import yaml
class get_yaml_data():
    def __init__(self,file):
        self.file=file

    def get_list_data(self):
        f = open(self.file, "r", encoding="utf8")
        o = yaml.load(f.read())
        dict={}
        for i in o.keys():
            if isinstance(o[i],list):
                o[i]=tuple(o[i])
            dict[i]=o[i]
            # dict[i]=tuple(o[i])
        # c = tuple(o["huiyuanlogin"])
        # print(c, type(c))
        return dict

    def get_data(self):
        f = open(self.file, "r", encoding="utf8")
        o = yaml.load(f.read())
        return o
