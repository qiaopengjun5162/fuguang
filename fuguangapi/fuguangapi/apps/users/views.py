# from rest_framework_jwt.views import ObtainJSONWebToken
import logging

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from fuguangapi.utils.tencentcloudapi import TencentCloudAPI,TencentCloudSDKException
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoginAPIView(TokenObtainPairView):
    """用户登录视图"""
    def post(self, request, *args, **kwargs):
        # 校验用户操作验证码成功以后的ticket临时票据
        print("login apiview")
        try:
            api = TencentCloudAPI()
            result = api.captcha(
                request.data.get("ticket"),
                request.data.get("randstr"),
                request._request.META.get("REMOTE_ADDR"),
            )
            if result:
                # 验证通过
                print("验证通过")
                # 登录实现代码，调用父类实现的登录视图方法
                return super().post(request, *args, **kwargs)
            else:
                # 如果返回值不是True，则表示验证失败
                raise TencentCloudSDKException
        except TencentCloudSDKException as err:
            logging.error("TencentCloudSDKException", err)
            return Response({"errmsg": "验证码校验失败！"}, status=status.HTTP_400_BAD_REQUEST)