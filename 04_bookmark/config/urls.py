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
from django.urls import path, include

urlpatterns = [
    # 대학병원에서 외과에 문진을 가야하는 경우, 바로 외과에 가는게 아니라 접수 중앙 로비에 접수하고 거기서 간호사와 직원분이 안내를 1차로 해준다.
    # 그리고 외과에 가면 2차로 간호사 접수를 또 해준다.
    # 위의 예처럼 url 동작방식도 같다.
    # 1차 -> 2차 -> 3차
    # http://127.0.0.1/bookmark/?
    # http://127.0.0.1/중앙창구/외과
    # http://127.0.0.1/중앙창구/내과
    # 주소 설계가 필요하다.
    # 여기서 1차 URL을 설계해준것이다.
    path('bookmark/', include('bookmark.urls')), # 슬래쉬 꼭 붙여야한다.
    # http://127.0.0.1/admin/
    path('admin/', admin.site.urls),
]
