"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/8 上午9:00
@Software : PyCharm
@File     : urls.py.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path("demo/", views.HomeAPIView.as_view()),
]
