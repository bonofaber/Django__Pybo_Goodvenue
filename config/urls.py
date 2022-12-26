"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include   #URL 한번에 모두 include
from goodvenue.views import base_views

#from goodvenue import views  #URL 매핑마다 추가 필요

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('goodvenue/', views.index), #URL 매핑마다 추가 필요
    path('goodvenue/', include('goodvenue.urls')),  #URL 한번에 모두 include
    path('common/', include('common.urls')),  # 로그인 로그아웃 기능 등
    # http://localhost:8000/common/ 로 시작 URL은 모두 common/urls.py 파일을참조
    path('', base_views.index, name='index'),  # 루트 '/' (http://localhost:8000/)에 해당되는 path
]
