import constants
from rest_framework.generics import ListAPIView
from .models import Nav
from .serializers import NavModelSerializer


class HeaderNavListAPIView(ListAPIView):
    """
    头部导航
    """
    queryset = Nav.objects.filter(is_delete=False, is_show=True, position=constants.NAV_HEADER).order_by("orders", "-id")[:constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    """
    脚部导航
    """
    queryset = Nav.objects.filter(is_delete=False, is_show=True, position=constants.NAV_FOOTER).order_by("orders", "-id")[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer
