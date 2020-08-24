# -*- coding: utf-8 -*-

import requests, sys, json
import urllib3

urllib3.disable_warnings()

###填写参数###

# Corpid是企业号的标识
Corpid = "wwb8ed5a7f6e7f8d71"

# Secret是管理组凭证密钥
Secret = "oJkYgiD-vzFQ97c7Xyd8M00Fmc2j7teuvYWcgphyj9E"

# 应用ID
Agentid = "1000002"

# token_config文件放置路径
Token_config = r'/tmp/zabbix_wechat_config.json'


###下面的代码都不需要动###


def GetTokenFromServer(Corpid, Secret):
    """获取access_token"""
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid": Corpid,
        "corpsecret": Secret
    }
    r = requests.get(url=Url, params=Data, verify=False)
    print(r.json())
    if r.json()['errcode'] != 0:
        return False
    else:
        Token = r.json()['access_token']
        file = open(Token_config, 'w')
        file.write(r.text)
        file.close()
        return Token


def SendMessage(Partyid, Subject, Content):
    """发送消息"""
    # 获取token信息
    # try:
    #     file = open(Token_config, 'r')
    #     Token = json.load(file)['access_token']
    #     file.close()
    # except:
    #     Token = GetTokenFromServer(Corpid, Secret)
    Token = "Xai0aEB0892UnyONmRIIsra1N30rCngdqtYG7tce7PjNxnHYckMoe9VAy9hFs4J4yIJfjmkwuhYsCRagqD3suZ0xiriY6mW56gv9qZ1y2UCoxtR4EXvcHVmv8W2MMhp0WYhIwPm4cmIb5ZNzr8_m77rjQL_O77K-mSitYomnHkwfM2_pLF7IRL2LDEcX6c795jczKH7jFlw-pYHMtHhqKw"
    # 发送消息
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        #"toparty": Partyid,
        "msgtype": "text",
        "agentid": Agentid,
        "text": {"content": Subject + '\n' + Content},
        "safe": "0"
    }
    r = requests.post(url=Url, data=json.dumps(Data), verify=False)

    # 如果发送失败，将重试三次
    n = 1
    while r.json()['errcode'] != 0 and n < 4:
        n = n + 1
        #Token = GetTokenFromServer(Corpid, Secret)
        if Token:
            Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
            r = requests.post(url=Url, data=json.dumps(Data), verify=False)
            print(r.json())

    return r.json()


if __name__ == '__main__':
    # 部门id
    Partyid = '20'
    # 消息标题
    Subject = '自应用程序代码测试'
    # 消息内容
    Content = 'str(sys.argv[3])'
    Status = SendMessage(Partyid, Subject, Content)
    print(Status)