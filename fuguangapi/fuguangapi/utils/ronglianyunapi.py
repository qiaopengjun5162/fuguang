"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/18 上午9:04
@Software : PyCharm
@File     : ronglianyunapi.py
"""
import json
from ronglian_sms_sdk import SmsSDK
from django.conf import settings


def send_sms(tid, mobile, datas):
    """
    发送短信
    https://doc.yuntongxun.com/pe/5f029ae7a80948a1006e776e
    @params tid: 模板ID，默认测试使用1
    @params mobile: 接收短信的手机号，多个手机号使用都逗号隔开
            单个号码： mobile="13312345678"
            多个号码： mobile="13312345678,13312345679,...."
    @params datas: 短信模板的参数列表
            例如短信模板为： 【云通讯】您的验证码是{1}，请于{2}分钟内正确输入。
            则datas=("123456",5,)
    """
    ronglianyun = settings.RONGLIANYUN
    sdk = SmsSDK(ronglianyun.get("accId"), ronglianyun.get("accToken"), ronglianyun.get("appId"))
    resp = sdk.sendMessage(tid, mobile, datas)
    response = json.loads(resp)
    print(response, type(response))
    return response.get("statusCode") == "000000"