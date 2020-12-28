"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# include를 임포트하고
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path를 하나 추가해 photo.urls를 연결해준다.
    # 이 때 URL 패턴을 ''로 설정하면 photo 앱이 메인 페이지로 동작한다.
    path('', include('photo.urls')),
]
# 5.3.8 템플릿 분리와 확장 -> base.html로 이동
