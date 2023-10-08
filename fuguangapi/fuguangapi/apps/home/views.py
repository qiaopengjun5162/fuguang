from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_redis import get_redis_connection


# Create your views here.


class HomeAPIView(APIView):
    def get(self, request):
        """测试接口"""
        print("hello")

        # 直接操作redis
        redis = get_redis_connection("session")
        # lrange brother 0 -1
        brother = redis.lrange("brother", 0, -1)
        print(brother)

        return Response(brother, status.HTTP_200_OK)
