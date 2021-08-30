# -*- coding: UTF-8 -*-
'''
@Project -> File   ：pyCode -> phoneMark
@Author ：ToualeCula
@Email ：1367642349@qq.com
@Date ：2021/8/29 18:30
@Desc ：
'''
import time,requests

class PhoneMark:
    def __init__(self,isDebug = False):
        self.isDebug = isDebug

    def getCaptcha(self):
        ''':cvar
        :return
            captcha picture
            with cookie
        '''

        url = "http://www.opene164.org.cn/mark/query/captcha.html?{}".format(int(time.time() * 1000))

        headers = {
            'Accept': '''text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-'exchange;v=b3;q=0.9''',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'www.opene164.org.cn',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }

        res = requests.get(url=url, headers=headers)
        try:
            captcha = res.content
            self.cookie = res.headers['Set-Cookie'].replace('; Path=/; HttpOnly','')

            if(self.isDebug):

                print("PhoneMark:")
                print("     init:")
                print("         cookie:",self.cookie)
                with open('temp.gif', "wb") as code:
                    code.write(captcha)
        except:
            captcha = ''
            self.cookie = ''
            print("!!! error: loacl -> PhoneMark.init   result: -> captcha = cookie = NULL")

        return captcha

    def selectPhone(self,phone,mark,proxies={}):
        url = 'http://www.opene164.org.cn/mark/data.do'

        data = 'phone={}&captcha={}'.format(phone,mark)

        headers = {
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control':'no-cachev',
            'Connection':'keep-alive',
            'Content-Length':'31',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':self.cookie,
            'DNT':'1',
            'Host':'www.opene164.org.cn',
            'Origin':'http://www.opene164.org.cn',
            'Pragma':'no-cache',
            'Referer':'http://www.opene164.org.cn/mark/index.html',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
            'X-Requested-With':'XMLHttpRequest'
        }

        res = requests.request('POST', url, data=data, headers=headers,proxies=proxies)
        return res.text



