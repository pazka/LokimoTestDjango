"""LokimoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from LokimoTest.LokimoTest.api import ad_api
from LokimoTest.LokimoTest.services.config import get_config

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Swagger config
if get_config("debug"):
    schema_view = get_schema_view(
        openapi.Info(
            title=get_config("project_name"),
            default_version="0.0.1",
            description=get_config("project_name") + "API description",
            contact=openapi.Contact(email="alexandre.weisser@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                       name='schema-json'),
    urlpatterns += url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    urlpatterns += url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

urlpatterns += path('ad/', include(ad_api.urls)),
