"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/13 下午3:14
@Software : PyCharm
@File     : views.py
"""
import constants
from rest_framework.generics import ListAPIView as DRFListAPIView
# cache_page是django提供给开发者使用的一个缓存类，专门缓存数据，以装饰器的方式提供操作
from django.views.decorators.cache import cache_page
# cache_page默认只能装饰函数视图，但是我们现在使用的普遍都是类视图，
# 所以又提供了一个method_decorators给开发者在不改动源码的情况下，就可以使用装饰器装饰一个类视图/类方法了
from django.utils.decorators import method_decorator


class ListAPIView(DRFListAPIView):
    """列表缓存视图类"""
    @method_decorator(cache_page(constants.LIST_PAGE_CACHE_TIME))
    def get(self, request, *args, **kwargs):
        # 重写ListAPIView的get方法，但是不改动源代码。仅仅装饰而已
        return super().get(request, *args, **kwargs)