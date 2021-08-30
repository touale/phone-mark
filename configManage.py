# -*- coding: UTF-8 -*-
'''
@Project -> File   ：pyCode -> configManage
@Author ：ToualeCula
@Email ：1367642349@qq.com
@Date ：2021/8/29 20:45
@Desc ：
'''

class ConfigManager:
    def __init__(self):

        # 是否debug模式
        self.isDebug = True

        # IP获取 和 白名单添加 -> 官网生成的
        self.ipApi = "http://tiqu.pyhttp.taolop.com/getip?count=1&neek=9123&type=1&yys=0&port=1&sb=&mr=2&sep=1&pack=2417"
        self.addIpApi = "http://pycn.yapi.3866866.com/index/index/save_white?neek=9123&appkey=70690e8a700fe2b06bd28e5943c5f496&white="

        # 联众账户和密码
        self.lianzhongUser = "Sanday001"
        self.lianzhongPass = "Xu/*-.a1"
        self.workId = 'AzVgdMDnmRkvdLc3lbwJIRrtR0PZxqhiHEvZY1zg'

        # 查询失败 -> 查询最大次数
        self.maxSelect = 1

        # 单个ip使用次数
        self.maxUse = 3



