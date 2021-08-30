# -*- coding: UTF-8 -*-
'''
@Project -> File   ：pyCode -> ipManage
@Author ：ToualeCula
@Email ：1367642349@qq.com
@Date ：2021/8/29 19:06
@Desc ：
'''

import requests
import threading,time

class IpManage:
    def __init__(self,ipApi,addIpApi,maxUse):
        threading.Thread.__init__(self)
        self.threadLock = threading.Lock()
        self.api = ipApi
        self.addIpApi = addIpApi
        self.proxies = {}
        self.maxUse = maxUse
        self.isUse = 0

    def getmidstring(self,html, start_str, end):
        start = html.find(start_str)
        if start >= 0:
            start += len(start_str)
            end = html.find(end, start)
            if end >= 0:
                return html[start:end].strip()

    def addIp(self,ip):
        url = self.addIpApi + self.getmidstring(ip,'IP[',']')
        requests.get(url=url)



    def refreshIp(self):
        self.isUse = 0
        res = requests.get(url=self.api)

        if(res.text.find('白名单校验失败') != -1):
            self.addIp(res.text)
            res = requests.get(url=self.api)
            if (res.text.find('白名单校验失败') != -1):
                self.proxies = {}
                return


        self.proxies = {
            "http": "http://{}".format(res.text.replace('\r\n',''))
        }
        return res.text

    def getIp(self):
        self.threadLock.acquire()
        if(self.proxies == {} or self.isUse > self.maxUse):
            if(self.refreshIp().find('请在1秒后再次请求') != -1):
                time.sleep(1)
                self.refreshIp()

        self.isUse += 1
        self.threadLock.release()
        return self.proxies

