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
    path("nav/header/", views.HeaderNavListAPIView.as_view()),
    path("nav/footer/", views.FooterNavListAPIView.as_view()),
    path("banner/", views.BannerListAPIView.as_view()),
]
