# -*- coding: UTF-8 -*-
'''
@Project -> File   ：pyCode -> captcha
@Author ：ToualeCula
@Email ：1367642349@qq.com
@Date ：2021/8/29 18:03
@Desc ：
'''

import requests
import base64,json

class Captcha:
    def __init__(self,user,pwd,workerTipsId):
        self.user = user
        self.pwd = pwd
        self.id = workerTipsId
        return

    def identify(self,imageData):

        api_post_url = 'https://v2-api.jsdama.com/upload'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Connection': 'keep-alive',
            'Host': 'v2-api.jsdama.com',
            'Upgrade-Insecure-Requests': '1'
        }


        data = {
            "softwareId": 26822,
            "softwareSecret": self.id,
            "username": self.user,
            "password": self.pwd,
            "captchaData": str(base64.b64encode(imageData), encoding = "utf8"),
            "captchaType": 1013,
            "captchaMinLength": 5,
            "captchaMaxLength": 5
        }

        r = requests.request('POST', api_post_url, json=data, headers=headers)
        try:
            js = json.loads(r.text)
            return js['data']['recognition'],r.text
        except:
            return '',r.text
