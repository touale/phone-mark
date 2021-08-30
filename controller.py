# -*- coding: UTF-8 -*-
'''
@Project -> File   ：pyCode -> controller
@Author ：ToualeCula
@Email ：1367642349@qq.com
@Date ：2021/8/29 20:52
@Desc ：
'''

from captcha import Captcha
from ipManage import IpManage
from configManage import ConfigManager
from phoneMark import PhoneMark
import json

class Controller:
    def __init__(self,isDebug = False):

        # config init
        configManage = ConfigManager()

        # IP init
        self.ipManage = IpManage(configManage.ipApi,
                                 configManage.addIpApi,
                                 configManage.maxUse)

        # captcha init
        self.captcha = Captcha(configManage.lianzhongUser,
                          configManage.lianzhongPass,
                          configManage.workId)

        # Max select for one
        self.maxSelect = configManage.maxSelect

        self.isDebug = isDebug


    def selectIn(self,phone):

        phoneMark = PhoneMark(isDebug=self.isDebug)
        captPic = phoneMark.getCaptcha()

        mark,identifyResult = self.captcha.identify(captPic)

        if(self.isDebug):print("mark == " + mark,identifyResult)

        if (mark == ''): return identifyResult

        ip = self.ipManage.getIp()

        if(self.isDebug):print(" ip Use:",ip)

        res = phoneMark.selectPhone(phone, mark, proxies=ip)

        return res

    def select(self,phone):
        for i in range(self.maxSelect):
            try:
                res = self.selectIn(phone)
            except:
                continue

            if(self.isDebug):print("    result:" + res)

            # 由于网站的code不统一，且json格式不统一，故采用字符比较
            if(res.find('您的当天查询次数已达上限，请明天继续查询') != -1):
                print("**** 已自动切换ip")
                self.ipManage.refreshIp()
                continue
            try:
                js = json.loads(res)
                if(js['status'] == 200):break
            except:
                continue

        return res

