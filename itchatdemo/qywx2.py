import json
import requests

Secret = "oJkYgiD-vzFQ97c7Xyd8M00Fmc2j7teuvYWcgphyj9E"
corpid = 'wwb8ed5a7f6e7f8d71'
url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'

getr = requests.get(url=url.format(corpid,Secret))
#
# print(r.json())
# {'errcode': 0, 'errmsg': 'ok', 'access_token': 't2HxARFMOgge-neHJwYXe4MrIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg', 'expires_in': 7200}

access_token = getr.json().get('access_token')
print(access_token)

# access_token ='t2HxARFMOgge-neHJwYXe4MrIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg'

#access_token ='t2HxARFMOgge-neHJwYXe4MrIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg'

data = {
   "touser" : "JiChuang|JiChuang",   # 向这些用户账户发送
   # "toparty" : "PartyID1|PartyID2",   # 向这些部门发送
   "msgtype" : "text",
   "agentid" : 1000002,                       # 应用的 id 号
   "text" : {
       "content" : "一看到你，我这张丑脸就泛起微笑^_^。"
   },
   "safe":0
}


r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),data=json.dumps(data))
print(r.json())