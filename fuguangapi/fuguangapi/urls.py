"""
URL configuration for fuguangapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.views.static import serve  # 静态文件代理访问模块

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
#
# schema_view = get_schema_view(title='API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

from rest_framework.documentation import include_docs_urls

# yasg的视图配置类，用于生成api
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 接口文档的视图配置
schema_view = get_schema_view(
    openapi.Info(
        title="drf接口文档",  # 站点标题，必填
        default_version='v1.0,0',  # api版本，必填
        description="描述信息",  # 站点描述
        terms_of_service='htttp://www.moluo.net/',  # 团队博客网址
        contact=openapi.Contact(name="qiao", url="htttp://www.qiao.net/", email="1746259155@qq.com"),  # 联系邮箱地址
        license=openapi.License(name="开源协议名称", url="开源协议网地")  # 协议
    ),
    public=True,  # 是否外部站点
    # permission_classes=(rest_framework.permissions.AllowAny)  # 权限类
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    # path('docs/', schema_view, name='docs'),

    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('docs/', include_docs_urls(title='fuguang')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'uploads/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path('', include("home.urls")),
    path("users/", include("users.urls")),
]
