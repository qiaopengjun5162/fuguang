# from rest_framework_jwt.views import ObtainJSONWebToken
import logging

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from fuguangapi.utils.tencentcloudapi import TencentCloudAPI, TencentCloudSDKException
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User


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


# /users/mobile/(?P<mobile>1[3-9]\d{9})


class MobileAPIView(APIView):
    def get(self, request, mobile):
        """
        校验手机号是否已注册
        :param request:
        :param mobile: 手机号
        :return:
        """
        try:
            User.objects.get(mobile=mobile)
            return Response({"errmsg": "当前手机号已注册"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            # 如果查不到该手机号的注册记录，则证明手机号可以注册使用
            return Response({"errmsg": "OK"}, status=status.HTTP_200_OK)
