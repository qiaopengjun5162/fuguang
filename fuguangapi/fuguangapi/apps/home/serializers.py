"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/11 上午2:09
@Software : PyCharm
@File     : serializers.py
"""
from rest_framework import serializers
from .models import Nav


class NavModelSerializer(serializers.ModelSerializer):
    """
    导航菜单的序列化器
    """
    class Meta:
        model = Nav
        fields = ["name", "link", "is_http"]
