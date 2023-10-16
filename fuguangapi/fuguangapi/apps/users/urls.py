"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/15 上午9:49
@Software : PyCharm
@File     : urls.py
"""
from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()
    # path("login/", obtain_jwt_token, name="login"),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
